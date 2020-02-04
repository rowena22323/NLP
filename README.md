# NLP
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 16.1 자연어 처리가 필요한 상황\n",
    "- 주어진 데이터가 문자열이더라도 일정한 내부 구조를 갖추고 있으면 자연어처리를 할 필요가 없다.\n",
    "- 문서간 유사성을 측정하는데 매우 적합\n",
    "- 문서에서 정확한 정보와 사실을 추출하는 일은 매우 어려움\n",
    "- 자연어 처리 알고리즘이 작동하는 이유를 설명하기 어려운 경우가 많음\n",
    "- 자연어 처리는 학습 데이터가 많이 필요함."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 16.2 언어와 통계\n",
    "## 통계적 자연어 처리\n",
    "- 문제를 데이터와 숫자를 이용해 해결\n",
    "- 데이터셋과 연선 규모가 커지면서 통계적 자연어 처리에 기반한 방식이 두각.\n",
    "- 왜 작동하는지 설명하기가 어렵다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 16.8 n-gram\n",
    "- 연속된 단어 (절)을 자연어 처리에서는 n-gram이라고 한다. \n",
    "- bigram 을 단어로 취급하여 BoW특징값을 뽑고 단어 빈도와 문서 빈도 역수를 적용할 수 있다.\n",
    "- n-gram의 단점 : 학습에 필요한 데이터가 기하급수적으로 늘어남 "
   ]
  }
