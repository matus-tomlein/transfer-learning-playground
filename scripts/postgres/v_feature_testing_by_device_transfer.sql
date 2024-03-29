CREATE MATERIALIZED VIEW v_feature_testing_by_device_transfer_aggr AS
SELECT
r_accuracy AS accuracy,
type_of_transfer,
scaled_independently,
features,
SUM("abs_energy") AS "abs_energy",
SUM("absolute_sum_of_changes") AS "absolute_sum_of_changes",
SUM("approximate_entropy__m_2__r_0.1") AS "approximate_entropy__m_2__r_0.1",
SUM("approximate_entropy__m_2__r_0.3") AS "approximate_entropy__m_2__r_0.3",
SUM("approximate_entropy__m_2__r_0.5") AS "approximate_entropy__m_2__r_0.5",
SUM("approximate_entropy__m_2__r_0.7") AS "approximate_entropy__m_2__r_0.7",
SUM("approximate_entropy__m_2__r_0.9") AS "approximate_entropy__m_2__r_0.9",
SUM("ar_coefficient__k_10__coeff_0") AS "ar_coefficient__k_10__coeff_0",
SUM("ar_coefficient__k_10__coeff_1") AS "ar_coefficient__k_10__coeff_1",
SUM("ar_coefficient__k_10__coeff_2") AS "ar_coefficient__k_10__coeff_2",
SUM("ar_coefficient__k_10__coeff_3") AS "ar_coefficient__k_10__coeff_3",
SUM("ar_coefficient__k_10__coeff_4") AS "ar_coefficient__k_10__coeff_4",
SUM("augmented_dickey_fuller") AS "augmented_dickey_fuller",
SUM("autocorrelation__lag_0") AS "autocorrelation__lag_0",
SUM("autocorrelation__lag_1") AS "autocorrelation__lag_1",
SUM("autocorrelation__lag_2") AS "autocorrelation__lag_2",
SUM("autocorrelation__lag_3") AS "autocorrelation__lag_3",
SUM("autocorrelation__lag_4") AS "autocorrelation__lag_4",
SUM("autocorrelation__lag_5") AS "autocorrelation__lag_5",
SUM("autocorrelation__lag_6") AS "autocorrelation__lag_6",
SUM("autocorrelation__lag_7") AS "autocorrelation__lag_7",
SUM("autocorrelation__lag_8") AS "autocorrelation__lag_8",
SUM("autocorrelation__lag_9") AS "autocorrelation__lag_9",
SUM("binned_entropy__max_bins_10") AS "binned_entropy__max_bins_10",
SUM("count_above_mean") AS "count_above_mean",
SUM("count_below_mean") AS "count_below_mean",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_5",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_10") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_10",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_2") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_2",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_20") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_20",
SUM("cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_5") AS
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_5",
SUM("fft_coefficient__coeff_0") AS "fft_coefficient__coeff_0",
SUM("fft_coefficient__coeff_1") AS "fft_coefficient__coeff_1",
SUM("fft_coefficient__coeff_2") AS "fft_coefficient__coeff_2",
SUM("fft_coefficient__coeff_3") AS "fft_coefficient__coeff_3",
SUM("fft_coefficient__coeff_4") AS "fft_coefficient__coeff_4",
SUM("fft_coefficient__coeff_5") AS "fft_coefficient__coeff_5",
SUM("fft_coefficient__coeff_6") AS "fft_coefficient__coeff_6",
SUM("fft_coefficient__coeff_7") AS "fft_coefficient__coeff_7",
SUM("fft_coefficient__coeff_8") AS "fft_coefficient__coeff_8",
SUM("fft_coefficient__coeff_9") AS "fft_coefficient__coeff_9",
SUM("first_location_of_maximum") AS "first_location_of_maximum",
SUM("first_location_of_minimum") AS "first_location_of_minimum",
SUM("friedrich_coefficients__m_3__r_30__coeff_0") AS
"friedrich_coefficients__m_3__r_30__coeff_0",
SUM("friedrich_coefficients__m_3__r_30__coeff_1") AS
"friedrich_coefficients__m_3__r_30__coeff_1",
SUM("friedrich_coefficients__m_3__r_30__coeff_2") AS
"friedrich_coefficients__m_3__r_30__coeff_2",
SUM("friedrich_coefficients__m_3__r_30__coeff_3") AS
"friedrich_coefficients__m_3__r_30__coeff_3",
SUM("has_duplicate") AS "has_duplicate",
SUM("has_duplicate_max") AS "has_duplicate_max",
SUM("has_duplicate_min") AS "has_duplicate_min",
SUM("index_mass_quantile__q_0.1") AS "index_mass_quantile__q_0.1",
SUM("index_mass_quantile__q_0.2") AS "index_mass_quantile__q_0.2",
SUM("index_mass_quantile__q_0.3") AS "index_mass_quantile__q_0.3",
SUM("index_mass_quantile__q_0.4") AS "index_mass_quantile__q_0.4",
SUM("index_mass_quantile__q_0.6") AS "index_mass_quantile__q_0.6",
SUM("index_mass_quantile__q_0.7") AS "index_mass_quantile__q_0.7",
SUM("index_mass_quantile__q_0.8") AS "index_mass_quantile__q_0.8",
SUM("index_mass_quantile__q_0.9") AS "index_mass_quantile__q_0.9",
SUM("kurtosis") AS "kurtosis",
SUM("large_number_of_peaks__n_1") AS "large_number_of_peaks__n_1",
SUM("large_number_of_peaks__n_3") AS "large_number_of_peaks__n_3",
SUM("large_number_of_peaks__n_5") AS "large_number_of_peaks__n_5",
SUM("large_standard_deviation__r_0.0") AS "large_standard_deviation__r_0.0",
SUM("large_standard_deviation__r_0.05") AS "large_standard_deviation__r_0.05",
SUM("large_standard_deviation__r_0.1") AS "large_standard_deviation__r_0.1",
SUM("large_standard_deviation__r_0.15000000000000002") AS
"large_standard_deviation__r_0.15000000000000002",
SUM("large_standard_deviation__r_0.2") AS "large_standard_deviation__r_0.2",
SUM("large_standard_deviation__r_0.25") AS "large_standard_deviation__r_0.25",
SUM("large_standard_deviation__r_0.30000000000000004") AS
"large_standard_deviation__r_0.30000000000000004",
SUM("large_standard_deviation__r_0.35000000000000003") AS
"large_standard_deviation__r_0.35000000000000003",
SUM("large_standard_deviation__r_0.4") AS "large_standard_deviation__r_0.4",
SUM("large_standard_deviation__r_0.45") AS "large_standard_deviation__r_0.45",
SUM("last_location_of_maximum") AS "last_location_of_maximum",
SUM("last_location_of_minimum") AS "last_location_of_minimum",
SUM("length") AS "length",
SUM("longest_strike_above_mean") AS "longest_strike_above_mean",
SUM("longest_strike_below_mean") AS "longest_strike_below_mean",
SUM("max_langevin_fixed_point__m_3__r_30") AS
"max_langevin_fixed_point__m_3__r_30",
SUM("maximum") AS "maximum",
SUM("mean") AS "mean",
SUM("mean_abs_change") AS "mean_abs_change",
SUM("mean_abs_change_quantiles__qh_0.2__ql_0.0") AS
"mean_abs_change_quantiles__qh_0.2__ql_0.0",
SUM("mean_abs_change_quantiles__qh_0.2__ql_0.2") AS
"mean_abs_change_quantiles__qh_0.2__ql_0.2",
SUM("mean_abs_change_quantiles__qh_0.2__ql_0.4") AS
"mean_abs_change_quantiles__qh_0.2__ql_0.4",
SUM("mean_abs_change_quantiles__qh_0.2__ql_0.6") AS
"mean_abs_change_quantiles__qh_0.2__ql_0.6",
SUM("mean_abs_change_quantiles__qh_0.2__ql_0.8") AS
"mean_abs_change_quantiles__qh_0.2__ql_0.8",
SUM("mean_abs_change_quantiles__qh_0.4__ql_0.0") AS
"mean_abs_change_quantiles__qh_0.4__ql_0.0",
SUM("mean_abs_change_quantiles__qh_0.4__ql_0.2") AS
"mean_abs_change_quantiles__qh_0.4__ql_0.2",
SUM("mean_abs_change_quantiles__qh_0.4__ql_0.4") AS
"mean_abs_change_quantiles__qh_0.4__ql_0.4",
SUM("mean_abs_change_quantiles__qh_0.4__ql_0.6") AS
"mean_abs_change_quantiles__qh_0.4__ql_0.6",
SUM("mean_abs_change_quantiles__qh_0.4__ql_0.8") AS
"mean_abs_change_quantiles__qh_0.4__ql_0.8",
SUM("mean_abs_change_quantiles__qh_0.6__ql_0.0") AS
"mean_abs_change_quantiles__qh_0.6__ql_0.0",
SUM("mean_abs_change_quantiles__qh_0.6__ql_0.2") AS
"mean_abs_change_quantiles__qh_0.6__ql_0.2",
SUM("mean_abs_change_quantiles__qh_0.6__ql_0.4") AS
"mean_abs_change_quantiles__qh_0.6__ql_0.4",
SUM("mean_abs_change_quantiles__qh_0.6__ql_0.6") AS
"mean_abs_change_quantiles__qh_0.6__ql_0.6",
SUM("mean_abs_change_quantiles__qh_0.6__ql_0.8") AS
"mean_abs_change_quantiles__qh_0.6__ql_0.8",
SUM("mean_abs_change_quantiles__qh_0.8__ql_0.0") AS
"mean_abs_change_quantiles__qh_0.8__ql_0.0",
SUM("mean_abs_change_quantiles__qh_0.8__ql_0.2") AS
"mean_abs_change_quantiles__qh_0.8__ql_0.2",
SUM("mean_abs_change_quantiles__qh_0.8__ql_0.4") AS
"mean_abs_change_quantiles__qh_0.8__ql_0.4",
SUM("mean_abs_change_quantiles__qh_0.8__ql_0.6") AS
"mean_abs_change_quantiles__qh_0.8__ql_0.6",
SUM("mean_abs_change_quantiles__qh_0.8__ql_0.8") AS
"mean_abs_change_quantiles__qh_0.8__ql_0.8",
SUM("mean_abs_change_quantiles__qh_1.0__ql_0.0") AS
"mean_abs_change_quantiles__qh_1.0__ql_0.0",
SUM("mean_abs_change_quantiles__qh_1.0__ql_0.2") AS
"mean_abs_change_quantiles__qh_1.0__ql_0.2",
SUM("mean_abs_change_quantiles__qh_1.0__ql_0.4") AS
"mean_abs_change_quantiles__qh_1.0__ql_0.4",
SUM("mean_abs_change_quantiles__qh_1.0__ql_0.6") AS
"mean_abs_change_quantiles__qh_1.0__ql_0.6",
SUM("mean_abs_change_quantiles__qh_1.0__ql_0.8") AS
"mean_abs_change_quantiles__qh_1.0__ql_0.8",
SUM("mean_autocorrelation") AS "mean_autocorrelation",
SUM("mean_change") AS "mean_change",
SUM("mean_second_derivate_central") AS "mean_second_derivate_central",
SUM("median") AS "median",
SUM("minimum") AS "minimum",
SUM("number_cwt_peaks__n_1") AS "number_cwt_peaks__n_1",
SUM("number_cwt_peaks__n_5") AS "number_cwt_peaks__n_5",
SUM("number_peaks__n_1") AS "number_peaks__n_1",
SUM("number_peaks__n_3") AS "number_peaks__n_3",
SUM("number_peaks__n_5") AS "number_peaks__n_5",
SUM("percentage_of_reoccurring_datapoints_to_all_datapoints") AS
"percentage_of_reoccurring_datapoints_to_all_datapoints",
SUM("percentage_of_reoccurring_values_to_all_values") AS
"percentage_of_reoccurring_values_to_all_values",
SUM("quantile__q_0.1") AS "quantile__q_0.1",
SUM("quantile__q_0.2") AS "quantile__q_0.2",
SUM("quantile__q_0.3") AS "quantile__q_0.3",
SUM("quantile__q_0.4") AS "quantile__q_0.4",
SUM("quantile__q_0.6") AS "quantile__q_0.6",
SUM("quantile__q_0.7") AS "quantile__q_0.7",
SUM("quantile__q_0.8") AS "quantile__q_0.8",
SUM("quantile__q_0.9") AS "quantile__q_0.9",
SUM("range_count__max_1__min_-1") AS "range_count__max_1__min_-1",
SUM("ratio_value_number_to_time_series_length") AS
"ratio_value_number_to_time_series_length",
SUM("sample_entropy") AS "sample_entropy",
SUM("skewness") AS "skewness",
SUM("spkt_welch_density__coeff_2") AS "spkt_welch_density__coeff_2",
SUM("spkt_welch_density__coeff_5") AS "spkt_welch_density__coeff_5",
SUM("spkt_welch_density__coeff_8") AS "spkt_welch_density__coeff_8",
SUM("standard_deviation") AS "standard_deviation",
SUM("sum_of_reoccurring_data_points") AS "sum_of_reoccurring_data_points",
SUM("sum_of_reoccurring_values") AS "sum_of_reoccurring_values",
SUM("sum_values") AS "sum_values",
SUM("symmetry_looking__r_0.0") AS "symmetry_looking__r_0.0",
SUM("symmetry_looking__r_0.05") AS "symmetry_looking__r_0.05",
SUM("symmetry_looking__r_0.1") AS "symmetry_looking__r_0.1",
SUM("symmetry_looking__r_0.15000000000000002") AS
"symmetry_looking__r_0.15000000000000002",
SUM("symmetry_looking__r_0.2") AS "symmetry_looking__r_0.2",
SUM("symmetry_looking__r_0.25") AS "symmetry_looking__r_0.25",
SUM("symmetry_looking__r_0.30000000000000004") AS
"symmetry_looking__r_0.30000000000000004",
SUM("symmetry_looking__r_0.35000000000000003") AS
"symmetry_looking__r_0.35000000000000003",
SUM("symmetry_looking__r_0.4") AS "symmetry_looking__r_0.4",
SUM("symmetry_looking__r_0.45") AS "symmetry_looking__r_0.45",
SUM("symmetry_looking__r_0.5") AS "symmetry_looking__r_0.5",
SUM("symmetry_looking__r_0.55") AS "symmetry_looking__r_0.55",
SUM("symmetry_looking__r_0.6000000000000001") AS
"symmetry_looking__r_0.6000000000000001",
SUM("symmetry_looking__r_0.65") AS "symmetry_looking__r_0.65",
SUM("symmetry_looking__r_0.7000000000000001") AS
"symmetry_looking__r_0.7000000000000001",
SUM("symmetry_looking__r_0.75") AS "symmetry_looking__r_0.75",
SUM("symmetry_looking__r_0.8") AS "symmetry_looking__r_0.8",
SUM("symmetry_looking__r_0.8500000000000001") AS
"symmetry_looking__r_0.8500000000000001",
SUM("symmetry_looking__r_0.9") AS "symmetry_looking__r_0.9",
SUM("symmetry_looking__r_0.9500000000000001") AS
"symmetry_looking__r_0.9500000000000001",
SUM("time_reversal_asymmetry_statistic__lag_1") AS
"time_reversal_asymmetry_statistic__lag_1",
SUM("time_reversal_asymmetry_statistic__lag_2") AS
"time_reversal_asymmetry_statistic__lag_2",
SUM("time_reversal_asymmetry_statistic__lag_3") AS
"time_reversal_asymmetry_statistic__lag_3",
SUM("value_count__value_-inf") AS "value_count__value_-inf",
SUM("value_count__value_0") AS "value_count__value_0",
SUM("value_count__value_1") AS "value_count__value_1",
SUM("value_count__value_inf") AS "value_count__value_inf",
SUM("value_count__value_nan") AS "value_count__value_nan",
SUM("variance") AS "variance",
SUM("variance_larger_than_standard_deviation") AS "variance_larger_than_standard_deviation"

FROM (
  SELECT *,
  source_device_type || ' > ' || target_device_type AS type_of_transfer,
  ROUND(accuracy, 1) AS r_accuracy
  FROM v_results_feature_testing
) t
GROUP BY type_of_transfer, r_accuracy, scaled_independently, features;
