from argparse import ArgumentParser, Namespace


def get_cli_args():
    parser = ArgumentParser(
        description="Discord bot to run a game of Trouble Brewing, a Blood on the Clocktower script"
    )

    log_args = parser.add_argument_group(
        "Logging", description="Arguments relating to logging of bot activity"
    )
    log_args.add_argument(
        "--logging-level",
        type=str,
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
    )

    web_args = parser.add_argument_group(
        "Web Interface", description="Arguments for connecting to the web browser"
    )
    web_args.add_argument(
        "--browser",
        type=str,
        choices=["chrome", "firefox", "safari", "edge", "safari"],
        default="firefox",
    )

    return parser.parse_args()
