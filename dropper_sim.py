#!/usr/bin/env python3
import argparse
import logging
import sys
import subprocess

# Configure logging: log to console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("dropper_sim.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="DropperSim - Simulate post-exploitation persistence methods")
    parser.add_argument(
        "--method",
        choices=["cronjob", "systemd", "startup", "all"],
        required=True,
        help="Persistence method to simulate"
    )
    parser.add_argument(
        "--target",
        default="localhost",
        help="Target hostname or IP (default: localhost)"
    )
    parser.add_argument(
        "--cleanup",
        action="store_true",
        help="Remove previously deployed persistence mechanisms"
    )
    return parser.parse_args()

def deploy_cronjob():
    logger.info("Deploying cron job persistence simulation...")
    cron_entry = "* * * * * echo 'DropperSim persistence active' >> /tmp/dropper_sim.log\n"

    # Try to get current crontab for user
    try:
        current_crontab = subprocess.run(['crontab', '-l'], capture_output=True, text=True, check=False)
        cron_contents = current_crontab.stdout if current_crontab.returncode == 0 else ''
        print("Current crontab contents:")
        print(cron_contents if cron_contents else "[EMPTY]")
    except Exception as e:
        logger.error(f"Failed to get current crontab: {e}")
        return False

    if cron_entry.strip() in cron_contents:
        logger.info("Cron job persistence already present.")
        return True

    # Append new entry
    new_cron = cron_contents + cron_entry

    try:
        print("Attempting to update crontab with:")
        print(new_cron)
        proc = subprocess.run(['crontab', '-'], input=new_cron, text=True, check=True)
        logger.info("Cron job persistence deployed successfully.")
        return True
    except Exception as e:
        logger.error(f"Failed to deploy cron job persistence: {e}")
        return False

def cleanup_cronjob():
    logger.info("Removing dropper_sim cron job persistence...")
    try:
        current_crontab = subprocess.run(['crontab', '-l'], capture_output=True, text=True, check=False)
        if current_crontab.returncode != 0:
            logger.info("No crontab to clean up")
            return True

        lines = current_crontab.stdout.splitlines()
        filtered_lines = [line for line in lines if "dropper_sim.log" not in line]

        new_cron = '\n'.join(filtered_lines) + '\n'
        print("New crontab after cleanup will be:")
        print(new_cron if new_cron.strip() else "[EMPTY]")
        subprocess.run(['crontab', '-'], input=new_cron, text=True, check=True)
        logger.info("Cron job persistence removed successfully.")
        return True
    except Exception as e:
        logger.error(f"Failed to clean up cron job persistence: {e}")
        return False

def main():
    args = parse_args()
    logger.info(f"Starting DropperSim on target: {args.target} with method: {args.method}")
    if args.cleanup:
        logger.info("Cleanup flag detected - will attempt to remove persistence")
    else:
        logger.info("Will deploy persistence")

    if args.method == "cronjob" or args.method == "all":
        if args.cleanup:
            cleanup_cronjob()
        else:
            deploy_cronjob()
    else:
        logger.info(f"Method '{args.method}' not implemented yet. Skipping.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupted by user. Exiting...")
        sys.exit(0)

