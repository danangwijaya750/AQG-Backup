import argparse
import os
from os.path import dirname
import sys
sys.path.insert(1, dirname(dirname(sys.path[0])))

from src.util import file_handler


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--train_src',
        default=None,
        type=str,
        required=True,
        help='Train source file (e.g.: ./data/processed/train/squad_id_cased_source.txt)',
    )
    parser.add_argument(
        '--train_tgt',
        default=None,
        type=str,
        required=True,
        help='Train target file (e.g.: ./data/processed/train/squad_id_cased_source.txt)',
    )
    parser.add_argument(
        '--valid_src',
        default=None,
        type=str,
        required=False,
        help='Valid source file (e.g.: ./data/processed/valid/squad_id_cased_source.txt)',
    )
    parser.add_argument(
        '--valid_tgt',
        default=None,
        type=str,
        required=False,
        help='Valid target file (e.g.: ./data/processed/valid/squad_id_cased_source.txt)',
    )
    parser.add_argument(
        '--test_src',
        default=None,
        type=str,
        required=False,
        help='Test source file (e.g.: ./data/processed/test/squad_id_cased_source.txt)',
    )
    parser.add_argument(
        '--test_tgt',
        default=None,
        type=str,
        required=False,
        help='Test target file (e.g.: ./data/processed/test/squad_id_cased_source.txt)',
    )
    parser.add_argument(
        '--add_special_tokens',
        action='store_true',
        help='Boolean parameter to add special tokens (<s>, <sep>, </s>) or not',
    )
    args = parser.parse_args()

    DATASET_DIR_ROOT = './dataset/processed'
    SAVE_DIR_ROOT = './dataset/processed/huggingface'

    data_path_tuples = [('train', args.train_src, args.train_tgt),
                        ('val', args.valid_src, args.valid_tgt),
                        ('test', args.test_src, args.test_tgt)]
    for data_path_tuple in data_path_tuples:
        save_dir = f'{SAVE_DIR_ROOT}/{data_path_tuple[0]}'
        print(f'Data are saved in {save_dir}')
        os.makedirs(save_dir, exist_ok=True)
        source_data = file_handler.load_txt(data_path_tuple[1])
        target_data = file_handler.load_txt(data_path_tuple[2])
        assert len(source_data) == len(target_data), \
            f'Total number of lines of source and target data must be same! Found {len(source_data)} and {len(target_data)}'

        save_file_name = 'sentence_pairs_spec_tokens.txt' if args.add_special_tokens else 'sentence_pairs.txt'
        with open(f'{save_dir}/{save_file_name}', 'w') as f_out:
            for i in range(len(source_data)):
                if source_data[i].strip():
                    if args.add_special_tokens:
                        f_out.write(f'<s> {source_data[i].strip()} <sep> {target_data[i].strip()} </s>\n')
                    else:
                        f_out.write(f'{source_data[i].strip()} \t {target_data[i].strip()}\n')
