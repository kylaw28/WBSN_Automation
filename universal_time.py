from datetime import datetime


class UniversalTime:
    def real_time(self):
        u_t_c = datetime.utcnow()
        u_t_c = str(u_t_c)
        u_t_c = u_t_c.replace(' ', ':')
        reformat_utc = u_t_c.split('.',1)
        utc = reformat_utc[0]
        # print(utc)
        return utc


if __name__ == "__main__":
    run_time = UniversalTime()
    run_time.real_time()
