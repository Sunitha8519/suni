{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square of the numbers are: [4, 16, 36, 64, 100]\n",
      "cube of the numbers are: [8, 64, 216, 512, 1000]\n"
     ]
    }
   ],
   "source": [
    "list1=[2,4,6,8,10]\n",
    "square=[i**2 for i in list1]\n",
    "print('Square of the numbers are:',square)\n",
    "cube=[i**3 for i in list1]\n",
    "print('cube of the numbers are:',cube)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "16\n",
      "36\n",
      "64\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "for i in list1:\n",
    "    print(i**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "64\n",
      "216\n",
      "512\n",
      "1000\n"
     ]
    }
   ],
   "source": [
    "for i in list1:\n",
    "    print(i**3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
