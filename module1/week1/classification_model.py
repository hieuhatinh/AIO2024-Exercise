def is_validate_type(value, input_type):
    if not isinstance(value, input_type):
        raise TypeError(f"{value} must be {input_type.__name__}")
    return True


def is_gather_than_zero(value):
    return value > 0


def classification_model(tp, fp, fn):
    try:
        validate_tp = is_validate_type(tp, int)
        validate_fp = is_validate_type(fp, int)
        validate_fn = is_validate_type(fn, int)
        tp_gather_than_zero = is_gather_than_zero(tp)
        fp_gather_than_zero = is_gather_than_zero(fp)
        fn_gather_than_zero = is_gather_than_zero(fn)

        if validate_tp and validate_fp and validate_fn:
            if not (tp_gather_than_zero and
                    fp_gather_than_zero and
                    fn_gather_than_zero):
                raise ValueError('tp and fp and fn must be greater than zero')

            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1_score = 2 * (precision * recall) / (precision + recall)

            print(f'precision is {precision} \n'
                  f'recall    is {recall}    \n'
                  f'f1_score  is {f1_score}')
    except Exception as e:
        print(e)
        return


classification_model(tp=1, fp=0, fn=4)
