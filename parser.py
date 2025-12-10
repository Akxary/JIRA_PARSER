from collections import defaultdict
from dataclasses import dataclass
from datetime import timedelta
import json
from typing import cast
from bs4 import BeautifulSoup, Tag
from pathlib import Path
import re


@dataclass
class LogData:
    user: str
    time_spent: str
    comment: str

    @property
    def time_delta(self) -> timedelta:
        hours = 0
        minutes = 0
        days_find = re.findall("([\d]+)[ ]*days?", self.time_spent)
        if len(days_find) > 0:
            hours += int(days_find[0]) * 8
        hours_find = re.findall("([\d]+)[ ]*hours?", self.time_spent)
        if len(hours_find) > 0:
            hours += int(hours_find[0])
        minutes_find = re.findall("([\d]+)[ ]*minutes?", self.time_spent)
        if len(minutes_find) > 0:
            minutes += int(minutes_find[0])
        return timedelta(hours=hours, minutes=minutes)


def get_all_log_data(input_html: str) -> dict[str, timedelta]:
    bs = BeautifulSoup(input_html, features="html.parser")
    log_founds = bs.find_all("div", class_="issue-data-block")
    all_log_data = []
    for log_found in log_founds:
        all_log_data.append(parse_one_log(log_found))
    user_log_group: dict[str, timedelta] = defaultdict(lambda: timedelta())
    for log_data in all_log_data:
        user_log_group[log_data.user] += log_data.time_delta
    return user_log_group


def parse_one_log(user_log_issue: Tag) -> LogData:
    log_data = LogData(
        user=cast(
            Tag,
            user_log_issue.find("a", class_="user-hover user-avatar"),
        ).text.strip("\n "),
        time_spent=cast(
            Tag,
            user_log_issue.find("dd", class_="worklog-duration"),
        ).text.strip("\n "),
        comment=cast(
            Tag,
            user_log_issue.find("dd", class_="worklog-comment"),
        ).text.strip("\n "),
    )
    return log_data


def group_log_by_team(
    user_log_group: dict[str, timedelta],
    dev_set: set[str],
) -> dict[str, timedelta]:
    team_log_group: dict[str, timedelta] = {"dev": timedelta(), "an": timedelta()}

    for user, user_time in user_log_group.items():
        print(f"user: {user}, time spent: {user_time}")
        if user in dev_set:
            team_log_group["dev"] += user_time
        else:
            team_log_group["an"] += user_time
    return team_log_group


def main() -> None:
    input_html = Path("resources/input.html").read_text(encoding="utf-8")
    dev_set = set(
        json.loads(Path("resources/dev-set.json").read_text(encoding="utf-8"))
    )
    user_log_group = get_all_log_data(input_html)
    team_log_group = group_log_by_team(user_log_group, dev_set)
    for team, team_time in team_log_group.items():
        print(f"{team}: {team_time.total_seconds() / 60 / 60 / 8:.5f} чд")


if __name__ == "__main__":
    main()
