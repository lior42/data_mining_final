from pydantic import BaseSettings


class AppSettings(BaseSettings):
    data_dir: str = "data"
    log_dir: str = "logs"
    save_file: str = "my_model.h5"
    training_size: float = 0.7
    reps: int = 20
    tag_file: str = "model_tags.json"
    coherent_prediction: float = 0.7

    class Config:
        env_prefix = "DATA_MINING_FINAL_PROJ_"
        env_file = ".env"


app_settings = AppSettings()