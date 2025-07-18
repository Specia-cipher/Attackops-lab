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
        choices=["cronjob"],
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

    try:
        current_crontab = subprocess.run(['crontab', '-l'], capture_output=True, text=True, check=False)
        cron_contents = current_crontab.stdout if current_crontab.returncode == 0 else ''
        logger.info("Current crontab contents:")
        logger.info(cron_contents if cron_contents else "[EMPTY]")
    except Exception as e:
        logger.error(f"Failed to get current crontab: {e}")
        return False

    if cron_entry.strip() in cron_contents:
        logger.info("Cron job persistence already present.")
        return True

    new_cron = cron_contents + cron_entry

    try:
        subprocess.run(['crontab', '-'], input=new_cron, text=True, check=True)
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

        new_cron = '\n'.join(filtered_lines) + ('\n' if filtered_lines else '')
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
        cleanup_cronjob()
    else:
        logger.info("Will deploy persistence")
        deploy_cronjob()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupted by user. Exiting...")
        sys.exit(0)

