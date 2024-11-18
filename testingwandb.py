import wandb

wandb.init(
    project="your_project_name",
    config={
        "learning_rate": 0.001,
        "epochs": 10,
        "batch_size": 32,
    },
)

for epoch in range(10):
    training_loss = 0.05 * (10 - epoch)
    validation_loss = 0.06 * (10 - epoch)

    wandb.log({"epoch": epoch, "training_loss": training_loss, "validation_loss": validation_loss})

artifact = wandb.Artifact("source_code", type="code")
artifact.add_file("testingwandb.py")
wandb.log_artifact(artifact)

wandb.finish()
