import wandb
import random
import os

# login to wandb server

wandb.login(
    key="local-aacdfecd37907b0fc4ce6141132851b35b666ae7",
    host="https://wandb-lab.jms-lab.com/"
)

#Simulate runs
num_runs = 1
os.environ["WANDB_RUN_GROUP"] = "experiment-" + wandb.util.generate_id()

while num_runs <= 10:
    # start a new wandb run to track this script
    wandb.init(
        # set the wandb project where this run will be logged
        project="lab-project",
        
        # track hyperparameters and run metadata
        config={
        "learning_rate": 0.02,
        "architecture": "CNN",
        "dataset": "CIFAR-100",
        "epochs": 10,
        }
    )

    # simulate training
    epochs = 10
    offset = random.random() / 5
    for epoch in range(2, epochs):
        acc = 1 - 2 ** -epoch - random.random() / epoch - offset
        loss = 2 ** -epoch + random.random() / epoch + offset
        
        # log metrics to wandb
        wandb.log({"acc": acc, "loss": loss})
    
    # [optional] finish the wandb run, necessary in notebooks
    wandb.finish()

    num_runs += 1