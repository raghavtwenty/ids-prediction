import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class naiveBias:
    def calculate_prior(self, df, Y):
        classes = sorted(list(df[Y].unique()))
        prior = []
        for i in classes:
            prior.append(len(df[df[Y]==i])/len(df))
        return prior

    def calculate_likelihood_gaussian(self,df, feat_name, feat_val, Y, label):
        feat = list(df.columns)
        df = df[df[Y]==label]
        mean, std = df[feat_name].mean(), df[feat_name].std()
        p_x_given_y = (1 / (np.sqrt(2 * np.pi) * std)) *  np.exp(-((feat_val-mean)**2 / (2 * std**2 )))
        return p_x_given_y

    def naive_bayes_gaussian(self,df, X, Y):
        # get feature names
        features = list(df.columns)[:-1]

        # calculate prior
        prior = self.calculate_prior(df, Y)

        Y_pred = []
        # loop over every data sample
        for x in X:
            # calculate likelihood
            labels = sorted(list(df[Y].unique()))
            likelihood = [1]*len(labels)
            for j in range(len(labels)):
                for i in range(len(features)):
                    likelihood[j] *= self.calculate_likelihood_gaussian(df, features[i], x[i], Y, labels[j])

            # calculate posterior probability (numerator only)
            post_prob = [1]*len(labels)
            for j in range(len(labels)):
                post_prob[j] = likelihood[j] * prior[j]

            Y_pred.append(post_prob)

        return np.array(Y_pred) 






location = pd.read_csv("/Users/raghav/Documents/Programs/projects/ids_prediction/dataset/ids_dataset_updated.csv")

dataFrame = pd.DataFrame(location)


predictors = dataFrame.iloc[:,:-1].values  # Leave the last column alone
target = dataFrame.iloc[:,-1].values   # Select the last column alone


# 80 train : 20 test
predTrain, predTest, tarTrain, tarTest = train_test_split(
                                                                predictors,
                                                                target,
                                                                train_size=0.8,
                                                                test_size=0.2,
                                                                shuffle=True)


testInput = [[4,349950,14844034,76099589,158473,2540,4,4,663067,662932]] # Normal 
#testInput = [[1,2990,67970025,63263334,4240,1906,5,1,13782,13662]]   # BlackHole 
#testInput = [[1,1241,25263813,25832,188,236,4,1,3216,3106]]  # Tcp Syn 
#testInput = [[3,744,12647232,31974078,126060,241,4,3,127492,127392]]  # PortScan
#testInput = [[2,4571,113552526,94919832,6236,2757,5,3,24500,24272]]    # Diversion  
nb = naiveBias()



naiv = nb.naive_bayes_gaussian(dataFrame,testInput,Y="Label")

naiv = naiv[0]

for i in naiv:
    print(i)
print(naiv)

sums = sum(naiv)


name = ["Normal","Block hole","TCP SYN","port scan","Diversion"]
for i in range(len(naiv)):
    temp = (naiv[i]/sums)*100
    print(f"{name[i]} --- {temp:.2f}%")

