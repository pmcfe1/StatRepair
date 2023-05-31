from typing import Any, Optional

from debuggingbook.StatisticalDebugger import TarantulaDebugger, ContinuousSpectrumDebugger, RankingDebugger


class StatRepair(ContinuousSpectrumDebugger, RankingDebugger):

    def mostsimilarstmt(self, targetloc):
        pass

    def suspiciousness(self, event: Any) -> Optional[float]:
        failed = len(self.collectors_with_event(event, self.FAIL))
        not_in_failed = len(self.collectors_without_event(event, self.FAIL))
        not_in_passed = len(self.collectors_without_event(event, self.PASS))
        passed = len(self.collectors_with_event(event, self.PASS))

        try:
            # return failed / math.sqrt((failed + not_in_failed) * (failed + passed))
            return 2 * (failed + (not_in_passed / (passed + not_in_passed)))
        except ZeroDivisionError:
            return None
