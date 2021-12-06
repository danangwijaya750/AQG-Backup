for i in 0..20
do
  onmt_train -data 'data/processed/onmt/squad_id_split0.9_cased' -save_model 'models/checkpoints/onmt/gru_045_new' \
    -world_size 1 \
    -seed 42 \
    -save_checkpoint_steps 8025 \
    -word_vec_size 300 \
    -pre_word_vecs_enc 'data/processed/onmt/embeddings_cased.enc.pt' \
    -pre_word_vecs_dec 'data/processed/onmt/embeddings_cased.dec.pt' \
    -fix_word_vecs_enc \
    -fix_word_vecs_dec \
    -keep_checkpoint 2 \
    -optim 'adam' \
    -learning_rate 0.001 \
    -learning_rate_decay 0.95 \
    -start_decay_steps 16050 \
    -rnn_type GRU \
    -encoder_type brnn \
    -layers 2 \
    -global_attention mlp \
    -rnn_size 256 \
    -train_steps 32100 \
    -valid_steps 3210 \
    -batch_size 64 \
    -dropout 0.3
done
