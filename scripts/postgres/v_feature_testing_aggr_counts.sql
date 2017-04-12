CREATE OR REPLACE VIEW v_feature_testing_aggr_counts AS
SELECT accuracy, type_of_transfer, 'abs_energy' AS feature, "abs_energy" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'absolute_sum_of_changes' AS feature, "absolute_sum_of_changes" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'approximate_entropy__m_2__r_0.1' AS feature, "approximate_entropy__m_2__r_0.1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'approximate_entropy__m_2__r_0.3' AS feature, "approximate_entropy__m_2__r_0.3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'approximate_entropy__m_2__r_0.5' AS feature, "approximate_entropy__m_2__r_0.5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'approximate_entropy__m_2__r_0.7' AS feature, "approximate_entropy__m_2__r_0.7" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'approximate_entropy__m_2__r_0.9' AS feature, "approximate_entropy__m_2__r_0.9" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'ar_coefficient__k_10__coeff_0' AS feature, "ar_coefficient__k_10__coeff_0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'ar_coefficient__k_10__coeff_1' AS feature, "ar_coefficient__k_10__coeff_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'ar_coefficient__k_10__coeff_2' AS feature, "ar_coefficient__k_10__coeff_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'ar_coefficient__k_10__coeff_3' AS feature, "ar_coefficient__k_10__coeff_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'ar_coefficient__k_10__coeff_4' AS feature, "ar_coefficient__k_10__coeff_4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'augmented_dickey_fuller' AS feature, "augmented_dickey_fuller" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_0' AS feature, "autocorrelation__lag_0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_1' AS feature, "autocorrelation__lag_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_2' AS feature, "autocorrelation__lag_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_3' AS feature, "autocorrelation__lag_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_4' AS feature, "autocorrelation__lag_4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_5' AS feature, "autocorrelation__lag_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_6' AS feature, "autocorrelation__lag_6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_7' AS feature, "autocorrelation__lag_7" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_8' AS feature, "autocorrelation__lag_8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'autocorrelation__lag_9' AS feature, "autocorrelation__lag_9" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'binned_entropy__max_bins_10' AS feature, "binned_entropy__max_bins_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'count_above_mean' AS feature, "count_above_mean" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'count_below_mean' AS feature, "count_below_mean" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_0__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_10__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_11__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_12__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_13__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_14__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_1__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_2__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_3__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_4__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_5__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_6__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_7__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_8__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_10' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_10" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_2' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_20' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_20" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_5' AS feature, "cwt_coefficients__widths_(2, 5, 10, 20)__coeff_9__w_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_0' AS feature, "fft_coefficient__coeff_0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_1' AS feature, "fft_coefficient__coeff_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_2' AS feature, "fft_coefficient__coeff_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_3' AS feature, "fft_coefficient__coeff_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_4' AS feature, "fft_coefficient__coeff_4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_5' AS feature, "fft_coefficient__coeff_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_6' AS feature, "fft_coefficient__coeff_6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_7' AS feature, "fft_coefficient__coeff_7" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_8' AS feature, "fft_coefficient__coeff_8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'fft_coefficient__coeff_9' AS feature, "fft_coefficient__coeff_9" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'first_location_of_maximum' AS feature, "first_location_of_maximum" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'first_location_of_minimum' AS feature, "first_location_of_minimum" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'friedrich_coefficients__m_3__r_30__coeff_0' AS feature, "friedrich_coefficients__m_3__r_30__coeff_0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'friedrich_coefficients__m_3__r_30__coeff_1' AS feature, "friedrich_coefficients__m_3__r_30__coeff_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'friedrich_coefficients__m_3__r_30__coeff_2' AS feature, "friedrich_coefficients__m_3__r_30__coeff_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'friedrich_coefficients__m_3__r_30__coeff_3' AS feature, "friedrich_coefficients__m_3__r_30__coeff_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'has_duplicate' AS feature, "has_duplicate" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'has_duplicate_max' AS feature, "has_duplicate_max" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'has_duplicate_min' AS feature, "has_duplicate_min" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.1' AS feature, "index_mass_quantile__q_0.1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.2' AS feature, "index_mass_quantile__q_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.3' AS feature, "index_mass_quantile__q_0.3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.4' AS feature, "index_mass_quantile__q_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.6' AS feature, "index_mass_quantile__q_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.7' AS feature, "index_mass_quantile__q_0.7" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.8' AS feature, "index_mass_quantile__q_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'index_mass_quantile__q_0.9' AS feature, "index_mass_quantile__q_0.9" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'kurtosis' AS feature, "kurtosis" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_number_of_peaks__n_1' AS feature, "large_number_of_peaks__n_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_number_of_peaks__n_3' AS feature, "large_number_of_peaks__n_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_number_of_peaks__n_5' AS feature, "large_number_of_peaks__n_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.0' AS feature, "large_standard_deviation__r_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.05' AS feature, "large_standard_deviation__r_0.05" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.1' AS feature, "large_standard_deviation__r_0.1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.15000000000000002' AS feature, "large_standard_deviation__r_0.15000000000000002" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.2' AS feature, "large_standard_deviation__r_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.25' AS feature, "large_standard_deviation__r_0.25" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.30000000000000004' AS feature, "large_standard_deviation__r_0.30000000000000004" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.35000000000000003' AS feature, "large_standard_deviation__r_0.35000000000000003" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.4' AS feature, "large_standard_deviation__r_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'large_standard_deviation__r_0.45' AS feature, "large_standard_deviation__r_0.45" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'last_location_of_maximum' AS feature, "last_location_of_maximum" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'last_location_of_minimum' AS feature, "last_location_of_minimum" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'length' AS feature, "length" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'longest_strike_above_mean' AS feature, "longest_strike_above_mean" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'longest_strike_below_mean' AS feature, "longest_strike_below_mean" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'max_langevin_fixed_point__m_3__r_30' AS feature, "max_langevin_fixed_point__m_3__r_30" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'maximum' AS feature, "maximum" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean' AS feature, "mean" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change' AS feature, "mean_abs_change" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.2__ql_0.0' AS feature, "mean_abs_change_quantiles__qh_0.2__ql_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.2__ql_0.2' AS feature, "mean_abs_change_quantiles__qh_0.2__ql_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.2__ql_0.4' AS feature, "mean_abs_change_quantiles__qh_0.2__ql_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.2__ql_0.6' AS feature, "mean_abs_change_quantiles__qh_0.2__ql_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.2__ql_0.8' AS feature, "mean_abs_change_quantiles__qh_0.2__ql_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.4__ql_0.0' AS feature, "mean_abs_change_quantiles__qh_0.4__ql_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.4__ql_0.2' AS feature, "mean_abs_change_quantiles__qh_0.4__ql_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.4__ql_0.4' AS feature, "mean_abs_change_quantiles__qh_0.4__ql_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.4__ql_0.6' AS feature, "mean_abs_change_quantiles__qh_0.4__ql_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.4__ql_0.8' AS feature, "mean_abs_change_quantiles__qh_0.4__ql_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.6__ql_0.0' AS feature, "mean_abs_change_quantiles__qh_0.6__ql_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.6__ql_0.2' AS feature, "mean_abs_change_quantiles__qh_0.6__ql_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.6__ql_0.4' AS feature, "mean_abs_change_quantiles__qh_0.6__ql_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.6__ql_0.6' AS feature, "mean_abs_change_quantiles__qh_0.6__ql_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.6__ql_0.8' AS feature, "mean_abs_change_quantiles__qh_0.6__ql_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.8__ql_0.0' AS feature, "mean_abs_change_quantiles__qh_0.8__ql_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.8__ql_0.2' AS feature, "mean_abs_change_quantiles__qh_0.8__ql_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.8__ql_0.4' AS feature, "mean_abs_change_quantiles__qh_0.8__ql_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.8__ql_0.6' AS feature, "mean_abs_change_quantiles__qh_0.8__ql_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_0.8__ql_0.8' AS feature, "mean_abs_change_quantiles__qh_0.8__ql_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_1.0__ql_0.0' AS feature, "mean_abs_change_quantiles__qh_1.0__ql_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_1.0__ql_0.2' AS feature, "mean_abs_change_quantiles__qh_1.0__ql_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_1.0__ql_0.4' AS feature, "mean_abs_change_quantiles__qh_1.0__ql_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_1.0__ql_0.6' AS feature, "mean_abs_change_quantiles__qh_1.0__ql_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_abs_change_quantiles__qh_1.0__ql_0.8' AS feature, "mean_abs_change_quantiles__qh_1.0__ql_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_autocorrelation' AS feature, "mean_autocorrelation" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_change' AS feature, "mean_change" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'mean_second_derivate_central' AS feature, "mean_second_derivate_central" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'median' AS feature, "median" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'minimum' AS feature, "minimum" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'number_cwt_peaks__n_1' AS feature, "number_cwt_peaks__n_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'number_cwt_peaks__n_5' AS feature, "number_cwt_peaks__n_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'number_peaks__n_1' AS feature, "number_peaks__n_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'number_peaks__n_3' AS feature, "number_peaks__n_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'number_peaks__n_5' AS feature, "number_peaks__n_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'percentage_of_reoccurring_datapoints_to_all_datapoints' AS feature, "percentage_of_reoccurring_datapoints_to_all_datapoints" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'percentage_of_reoccurring_values_to_all_values' AS feature, "percentage_of_reoccurring_values_to_all_values" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.1' AS feature, "quantile__q_0.1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.2' AS feature, "quantile__q_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.3' AS feature, "quantile__q_0.3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.4' AS feature, "quantile__q_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.6' AS feature, "quantile__q_0.6" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.7' AS feature, "quantile__q_0.7" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.8' AS feature, "quantile__q_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'quantile__q_0.9' AS feature, "quantile__q_0.9" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'range_count__max_1__min_-1' AS feature, "range_count__max_1__min_-1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'ratio_value_number_to_time_series_length' AS feature, "ratio_value_number_to_time_series_length" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'sample_entropy' AS feature, "sample_entropy" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'skewness' AS feature, "skewness" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'spkt_welch_density__coeff_2' AS feature, "spkt_welch_density__coeff_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'spkt_welch_density__coeff_5' AS feature, "spkt_welch_density__coeff_5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'spkt_welch_density__coeff_8' AS feature, "spkt_welch_density__coeff_8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'standard_deviation' AS feature, "standard_deviation" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'sum_of_reoccurring_data_points' AS feature, "sum_of_reoccurring_data_points" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'sum_of_reoccurring_values' AS feature, "sum_of_reoccurring_values" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'sum_values' AS feature, "sum_values" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.0' AS feature, "symmetry_looking__r_0.0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.05' AS feature, "symmetry_looking__r_0.05" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.1' AS feature, "symmetry_looking__r_0.1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.15000000000000002' AS feature, "symmetry_looking__r_0.15000000000000002" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.2' AS feature, "symmetry_looking__r_0.2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.25' AS feature, "symmetry_looking__r_0.25" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.30000000000000004' AS feature, "symmetry_looking__r_0.30000000000000004" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.35000000000000003' AS feature, "symmetry_looking__r_0.35000000000000003" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.4' AS feature, "symmetry_looking__r_0.4" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.45' AS feature, "symmetry_looking__r_0.45" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.5' AS feature, "symmetry_looking__r_0.5" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.55' AS feature, "symmetry_looking__r_0.55" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.6000000000000001' AS feature, "symmetry_looking__r_0.6000000000000001" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.65' AS feature, "symmetry_looking__r_0.65" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.7000000000000001' AS feature, "symmetry_looking__r_0.7000000000000001" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.75' AS feature, "symmetry_looking__r_0.75" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.8' AS feature, "symmetry_looking__r_0.8" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.8500000000000001' AS feature, "symmetry_looking__r_0.8500000000000001" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.9' AS feature, "symmetry_looking__r_0.9" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'symmetry_looking__r_0.9500000000000001' AS feature, "symmetry_looking__r_0.9500000000000001" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'time_reversal_asymmetry_statistic__lag_1' AS feature, "time_reversal_asymmetry_statistic__lag_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'time_reversal_asymmetry_statistic__lag_2' AS feature, "time_reversal_asymmetry_statistic__lag_2" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'time_reversal_asymmetry_statistic__lag_3' AS feature, "time_reversal_asymmetry_statistic__lag_3" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'value_count__value_-inf' AS feature, "value_count__value_-inf" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'value_count__value_0' AS feature, "value_count__value_0" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'value_count__value_1' AS feature, "value_count__value_1" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'value_count__value_inf' AS feature, "value_count__value_inf" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'value_count__value_nan' AS feature, "value_count__value_nan" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'variance' AS feature, "variance" AS count FROM v_feature_testing_aggr UNION
SELECT accuracy, type_of_transfer, 'variance_larger_than_standard_deviation' AS feature, "variance_larger_than_standard_deviation" AS count FROM v_feature_testing_aggr
