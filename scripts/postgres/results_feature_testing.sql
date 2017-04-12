CREATE TABLE results_feature_testing (source_device INTEGER,
target_device INTEGER,
source_dataset INTEGER,
target_dataset INTEGER,
activities INTEGER,
feature INTEGER,
accuracy NUMERIC,
precision_recall_fscore_support TEXT,
confusion_matrix TEXT,
"abs_energy" NUMERIC,
"absolute_sum_of_changes" NUMERIC,
"approximate_entropy__m_2__r_0.1" NUMERIC,
"approximate_entropy__m_2__r_0.3" NUMERIC,
"approximate_entropy__m_2__r_0.5" NUMERIC,
"approximate_entropy__m_2__r_0.7" NUMERIC,
"approximate_entropy__m_2__r_0.9" NUMERIC,
"ar_coefficient__k_10__coeff_0" NUMERIC,
"ar_coefficient__k_10__coeff_1" NUMERIC,
"ar_coefficient__k_10__coeff_2" NUMERIC,
"ar_coefficient__k_10__coeff_3" NUMERIC,
"ar_coefficient__k_10__coeff_4" NUMERIC,
"augmented_dickey_fuller" NUMERIC,
"autocorrelation__lag_0" NUMERIC,
"autocorrelation__lag_1" NUMERIC,
"autocorrelation__lag_2" NUMERIC,
"autocorrelation__lag_3" NUMERIC,
"autocorrelation__lag_4" NUMERIC,
"autocorrelation__lag_5" NUMERIC,
"autocorrelation__lag_6" NUMERIC,
"autocorrelation__lag_7" NUMERIC,
"autocorrelation__lag_8" NUMERIC,
"autocorrelation__lag_9" NUMERIC,
"binned_entropy__max_bins_10" NUMERIC,
"count_above_mean" NUMERIC,
"count_below_mean" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_5" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_10" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_2" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_20" NUMERIC,
"cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_5" NUMERIC,
"fft_coefficient__coeff_0" NUMERIC,
"fft_coefficient__coeff_1" NUMERIC,
"fft_coefficient__coeff_2" NUMERIC,
"fft_coefficient__coeff_3" NUMERIC,
"fft_coefficient__coeff_4" NUMERIC,
"fft_coefficient__coeff_5" NUMERIC,
"fft_coefficient__coeff_6" NUMERIC,
"fft_coefficient__coeff_7" NUMERIC,
"fft_coefficient__coeff_8" NUMERIC,
"fft_coefficient__coeff_9" NUMERIC,
"first_location_of_maximum" NUMERIC,
"first_location_of_minimum" NUMERIC,
"friedrich_coefficients__m_3__r_30__coeff_0" NUMERIC,
"friedrich_coefficients__m_3__r_30__coeff_1" NUMERIC,
"friedrich_coefficients__m_3__r_30__coeff_2" NUMERIC,
"friedrich_coefficients__m_3__r_30__coeff_3" NUMERIC,
"has_duplicate" NUMERIC,
"has_duplicate_max" NUMERIC,
"has_duplicate_min" NUMERIC,
"index_mass_quantile__q_0.1" NUMERIC,
"index_mass_quantile__q_0.2" NUMERIC,
"index_mass_quantile__q_0.3" NUMERIC,
"index_mass_quantile__q_0.4" NUMERIC,
"index_mass_quantile__q_0.6" NUMERIC,
"index_mass_quantile__q_0.7" NUMERIC,
"index_mass_quantile__q_0.8" NUMERIC,
"index_mass_quantile__q_0.9" NUMERIC,
"kurtosis" NUMERIC,
"large_number_of_peaks__n_1" NUMERIC,
"large_number_of_peaks__n_3" NUMERIC,
"large_number_of_peaks__n_5" NUMERIC,
"large_standard_deviation__r_0.0" NUMERIC,
"large_standard_deviation__r_0.05" NUMERIC,
"large_standard_deviation__r_0.1" NUMERIC,
"large_standard_deviation__r_0.15000000000000002" NUMERIC,
"large_standard_deviation__r_0.2" NUMERIC,
"large_standard_deviation__r_0.25" NUMERIC,
"large_standard_deviation__r_0.30000000000000004" NUMERIC,
"large_standard_deviation__r_0.35000000000000003" NUMERIC,
"large_standard_deviation__r_0.4" NUMERIC,
"large_standard_deviation__r_0.45" NUMERIC,
"last_location_of_maximum" NUMERIC,
"last_location_of_minimum" NUMERIC,
"length" NUMERIC,
"longest_strike_above_mean" NUMERIC,
"longest_strike_below_mean" NUMERIC,
"max_langevin_fixed_point__m_3__r_30" NUMERIC,
"maximum" NUMERIC,
"mean" NUMERIC,
"mean_abs_change" NUMERIC,
"mean_abs_change_quantiles__qh_0.2__ql_0.0" NUMERIC,
"mean_abs_change_quantiles__qh_0.2__ql_0.2" NUMERIC,
"mean_abs_change_quantiles__qh_0.2__ql_0.4" NUMERIC,
"mean_abs_change_quantiles__qh_0.2__ql_0.6" NUMERIC,
"mean_abs_change_quantiles__qh_0.2__ql_0.8" NUMERIC,
"mean_abs_change_quantiles__qh_0.4__ql_0.0" NUMERIC,
"mean_abs_change_quantiles__qh_0.4__ql_0.2" NUMERIC,
"mean_abs_change_quantiles__qh_0.4__ql_0.4" NUMERIC,
"mean_abs_change_quantiles__qh_0.4__ql_0.6" NUMERIC,
"mean_abs_change_quantiles__qh_0.4__ql_0.8" NUMERIC,
"mean_abs_change_quantiles__qh_0.6__ql_0.0" NUMERIC,
"mean_abs_change_quantiles__qh_0.6__ql_0.2" NUMERIC,
"mean_abs_change_quantiles__qh_0.6__ql_0.4" NUMERIC,
"mean_abs_change_quantiles__qh_0.6__ql_0.6" NUMERIC,
"mean_abs_change_quantiles__qh_0.6__ql_0.8" NUMERIC,
"mean_abs_change_quantiles__qh_0.8__ql_0.0" NUMERIC,
"mean_abs_change_quantiles__qh_0.8__ql_0.2" NUMERIC,
"mean_abs_change_quantiles__qh_0.8__ql_0.4" NUMERIC,
"mean_abs_change_quantiles__qh_0.8__ql_0.6" NUMERIC,
"mean_abs_change_quantiles__qh_0.8__ql_0.8" NUMERIC,
"mean_abs_change_quantiles__qh_1.0__ql_0.0" NUMERIC,
"mean_abs_change_quantiles__qh_1.0__ql_0.2" NUMERIC,
"mean_abs_change_quantiles__qh_1.0__ql_0.4" NUMERIC,
"mean_abs_change_quantiles__qh_1.0__ql_0.6" NUMERIC,
"mean_abs_change_quantiles__qh_1.0__ql_0.8" NUMERIC,
"mean_autocorrelation" NUMERIC,
"mean_change" NUMERIC,
"mean_second_derivate_central" NUMERIC,
"median" NUMERIC,
"minimum" NUMERIC,
"number_cwt_peaks__n_1" NUMERIC,
"number_cwt_peaks__n_5" NUMERIC,
"number_peaks__n_1" NUMERIC,
"number_peaks__n_3" NUMERIC,
"number_peaks__n_5" NUMERIC,
"percentage_of_reoccurring_datapoints_to_all_datapoints" NUMERIC,
"percentage_of_reoccurring_values_to_all_values" NUMERIC,
"quantile__q_0.1" NUMERIC,
"quantile__q_0.2" NUMERIC,
"quantile__q_0.3" NUMERIC,
"quantile__q_0.4" NUMERIC,
"quantile__q_0.6" NUMERIC,
"quantile__q_0.7" NUMERIC,
"quantile__q_0.8" NUMERIC,
"quantile__q_0.9" NUMERIC,
"range_count__max_1__min_-1" NUMERIC,
"ratio_value_number_to_time_series_length" NUMERIC,
"sample_entropy" NUMERIC,
"skewness" NUMERIC,
"spkt_welch_density__coeff_2" NUMERIC,
"spkt_welch_density__coeff_5" NUMERIC,
"spkt_welch_density__coeff_8" NUMERIC,
"standard_deviation" NUMERIC,
"sum_of_reoccurring_data_points" NUMERIC,
"sum_of_reoccurring_values" NUMERIC,
"sum_values" NUMERIC,
"symmetry_looking__r_0.0" NUMERIC,
"symmetry_looking__r_0.05" NUMERIC,
"symmetry_looking__r_0.1" NUMERIC,
"symmetry_looking__r_0.15000000000000002" NUMERIC,
"symmetry_looking__r_0.2" NUMERIC,
"symmetry_looking__r_0.25" NUMERIC,
"symmetry_looking__r_0.30000000000000004" NUMERIC,
"symmetry_looking__r_0.35000000000000003" NUMERIC,
"symmetry_looking__r_0.4" NUMERIC,
"symmetry_looking__r_0.45" NUMERIC,
"symmetry_looking__r_0.5" NUMERIC,
"symmetry_looking__r_0.55" NUMERIC,
"symmetry_looking__r_0.6000000000000001" NUMERIC,
"symmetry_looking__r_0.65" NUMERIC,
"symmetry_looking__r_0.7000000000000001" NUMERIC,
"symmetry_looking__r_0.75" NUMERIC,
"symmetry_looking__r_0.8" NUMERIC,
"symmetry_looking__r_0.8500000000000001" NUMERIC,
"symmetry_looking__r_0.9" NUMERIC,
"symmetry_looking__r_0.9500000000000001" NUMERIC,
"time_reversal_asymmetry_statistic__lag_1" NUMERIC,
"time_reversal_asymmetry_statistic__lag_2" NUMERIC,
"time_reversal_asymmetry_statistic__lag_3" NUMERIC,
"value_count__value_-inf" NUMERIC,
"value_count__value_0" NUMERIC,
"value_count__value_1" NUMERIC,
"value_count__value_inf" NUMERIC,
"value_count__value_nan" NUMERIC,
"variance" NUMERIC,
"variance_larger_than_standard_deviation" NUMERIC);