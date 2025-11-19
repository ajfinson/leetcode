from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
from typing import List


class RateType(Enum):
    REGULAR = 'regular'
    DAILY_OVERTIME = 'dailyOvertime'


@dataclass
class WorkPeriod:
    start_time: datetime
    end_time: datetime


@dataclass
class DailyOvertimeRule:
    hours_threshold: float


@dataclass
class PaidHoursSegment:
    date: date
    hours: float
    rate_type: RateType

def calculate_daily_hours(
        work_periods: List[WorkPeriod],
        overtime_rule: DailyOvertimeRule
) -> List[PaidHoursSegment]:
    pass

# Example usage:
example_periods = [
    WorkPeriod(
        start_time=datetime(2024, 3, 18, 9, 0),  # 9:00 AM
        end_time=datetime(2024, 3, 18, 19, 0)  # 7:00 PM (10 hours)
    ),
    WorkPeriod(
        start_time=datetime(2024, 3, 19, 9, 0),  # 9:00 AM
        end_time=datetime(2024, 3, 19, 16, 0)  # 4:00 PM (7 hours)
    ),
    WorkPeriod(
        start_time=datetime(2024, 3, 19, 21, 0),  # 9:00 PM
        end_time=datetime(2024, 3, 19, 23, 0)  # 11:00 PM (2 hours)
    )
]

example_rule = DailyOvertimeRule(hours_threshold=8)

# Expected result:
expected_result = [
    # March 18 - Regular hours (8) + Overtime (2)
    PaidHoursSegment(date=date(2024, 3, 18), hours=8.0, rate_type=RateType.REGULAR),
    PaidHoursSegment(date=date(2024, 3, 18), hours=2.0, rate_type=RateType.DAILY_OVERTIME),
    # March 19 - Regular hours (8) + Overtime (1)
    PaidHoursSegment(date=date(2024, 3, 19), hours=8.0, rate_type=RateType.REGULAR),
    PaidHoursSegment(date=date(2024, 3, 19), hours=1.0, rate_type=RateType.DAILY_OVERTIME)
]