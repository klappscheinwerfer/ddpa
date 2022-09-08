import pandas as pd
import numpy as np

def get_links(df, out):
	np.savetxt(out + "links.txt", df["Attachments"].dropna().to_numpy() , fmt='%s')
