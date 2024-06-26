#     Copyright 2016-present CERN – European Organization for Nuclear Research
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from qf_lib.containers.dataframe.qf_dataframe import QFDataFrame


class SimpleReturnsDataFrame(QFDataFrame):
    """
    DataFrame containing simple returns.
    """
    @property
    def _constructor_sliced(self):
        from qf_lib.containers.series.simple_returns_series import SimpleReturnsSeries
        return SimpleReturnsSeries

    @property
    def _constructor(self):
        return SimpleReturnsDataFrame

    def aggregate_by_year(self):
        from qf_lib.common.utils.returns.get_aggregate_returns import get_aggregate_returns
        from qf_lib.common.enums.frequency import Frequency

        def agg_series_by_year(series):
            return get_aggregate_returns(series=series, convert_to=Frequency.YEARLY)

        annual_returns_df = self.apply(agg_series_by_year, axis=0)
        return annual_returns_df

    def to_simple_returns(self) -> "SimpleReturnsDataFrame":
        """
        Converts dataframe to the dataframe of simple returns. First date of prices in the returns timeseries won't
        be present.

        Returns
        -------
        SimpleReturnsDataFrame
            dataframe of simple returns
        """
        return self
