def single_sample_md_nre(y, y_hat, n, p):
    result_sample = (y**(1/n) - y_hat**(1/n))**p
    return result_sample


result_single_sample_1 = single_sample_md_nre(y=100, y_hat=99.5, n=2, p=1)
result_single_sample_2 = single_sample_md_nre(y=50, y_hat=49.5, n=2, p=1)
result_single_sample_3 = single_sample_md_nre(y=20, y_hat=19.5, n=2, p=1)

print(result_single_sample_1)
print(result_single_sample_2)
print(result_single_sample_3)
