#!/usr/bin/env node
import { exec } from "child_process";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import chalk from "chalk";
import boxen from "boxen";

// Create a visually appealing header
console.log(
  boxen(chalk.bold.greenBright("🌟 Welcome to Spam Detector CLI! 🌟"), {
    padding: 1,
    margin: 1,
    borderStyle: "double",
    borderColor: "yellow",
    align: "center",
  })
);

// Setup CLI arguments with `yargs`
const argv = yargs(hideBin(process.argv))
  .usage(
    chalk.cyanBright("Usage: spamdetector -e [email content]\n\n") +
      chalk.bold("Options:")
  )
  .option("e", {
    alias: "email",
    type: "string",
    description: chalk.greenBright("Email content to check for spam"),
    demandOption: true,
  })
  .example(
    chalk.cyanBright("spamdetector -e 'Congratulations! You've won a prize!'"),
    chalk.yellow("Analyze an email for spam content")
  )
  .help("h")
  .alias("h", "help")
  .epilog(chalk.magentaBright("Created by: maria kouchkar 🚀"))
  .argv;

// Analyze the email content if provided
console.log(
  chalk.yellow("\n🔍 Analyzing email content: ") +
    chalk.whiteBright.bold(`"${argv.email}"`)
);

// Call Python spam detection script
exec(
  `python spam_detector.py "${argv.email}"`,
  (error, stdout, stderr) => {
    if (error) {
      console.error(chalk.redBright("\n🚨 Error: "), chalk.red(error.message));
      return;
    }
    if (stderr) {
      console.error(chalk.redBright("\n🚨 Stderr: "), chalk.red(stderr));
      return;
    }

    // Display results in a styled box
    console.log(
      boxen(chalk.blueBright.bold(`\nResult:\n${stdout.trim()}\n`), {
        padding: 1,
        margin: 1,
        borderStyle: "round",
        borderColor: "blue",
      })
    );
  }
);