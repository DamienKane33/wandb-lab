import wandb
import random

# login to wandb server

wandb.login(
    key="local-aacdfecd37907b0fc4ce6141132851b35b666ae7",
    host="https://wandb-lab.jms-lab.com/"
)

#Simulate runs
total_num_runs =  0

group_name = "experiment-" + wandb.util.generate_id()

while total_num_runs <= 20:

    num_runs = random.randrange(5)

    group_name = "experiment-" + wandb.util.generate_id()

    while num_runs > 0:
        # start a new wandb run to track this script
        wandb.init(
            # set the wandb project where this run will be logged
            project="group-lab",
            group= group_name,
            
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

        num_runs -= 1
    
    total_num_runs += num_runs