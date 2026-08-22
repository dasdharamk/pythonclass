{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOh5muV1G0zoukgLEICX2Mq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dasdharamk/pythonclass/blob/main/numberguessinggameplay.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4t6X3THSWs7H",
        "outputId": "e1ecd081-57ab-4024-c1bc-1692c5976267"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🎮 Number Guessing Game\n",
            "I picked a number between 1 and 100.\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "number = random.randint(1, 100)\n",
        "\n",
        "print(\"🎮 Number Guessing Game\")\n",
        "print(\"I picked a number between 1 and 100.\")\n",
        "\n",
        "while True:\n",
        "    guess = int(input(\"Enter your guess: \"))\n",
        "\n",
        "    if guess < number:\n",
        "        print(\"Too low! Try again.\")\n",
        "    elif guess > number:\n",
        "        print(\"Too high! Try again.\")\n",
        "    else:\n",
        "        print(\"🎉 Correct! You guessed the number!\")\n",
        "        break"
      ]
    }
  ]
}