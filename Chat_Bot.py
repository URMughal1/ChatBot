{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Chat_Bot.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/URMughal1/ChatBot/blob/master/Chat_Bot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "LdOhyj98Og1G",
        "colab_type": "code",
        "outputId": "4edc45d6-f64b-4f4d-fb1b-49c1e8032b3e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        }
      },
      "source": [
        "'''\n",
        "Author:Umer Rehman\n",
        "Last Time changed: 09-10-2019\n",
        "'''\n",
        "\n",
        "import sys\n",
        "from datetime import datetime\n",
        "\n",
        "# Making Time stemped File name\n",
        "dateTimeObj = datetime.now()\n",
        "timestampStr = dateTimeObj.strftime(\"%d-%b-%Y_(%H-%M-%S)\")\n",
        "write_to_text=open(\"CH_\"+timestampStr+\".txt\",\"w+\")\n",
        "write_to_text.write(\"Time: \"+ timestampStr + \" \\n \")\n",
        "\n",
        "#Check if the Input is Integer or not \n",
        "def Ask_Question(Question, C_input):\n",
        "    while (True):\n",
        "        try:\n",
        "            val = int(C_input)\n",
        "            break\n",
        "        except ValueError:\n",
        "            write_to_text.write(Question + \" \\n \")\n",
        "            print(Question)\n",
        "            C_input = input(\"Customer: \")\n",
        "            write_to_text.write(\"Customer: \"+ C_input + \" \\n \")\n",
        "            continue\n",
        "    return val\n",
        "\n",
        "#Getting Information about the trucks and their models \n",
        "def Truck_Information(Number):\n",
        "    write_to_text.write(\"Chatbot: What is the \"+Number+\" brand Name?\" + \" \\n \")\n",
        "    print(\"Chatbot: What is the \"+Number+\" brand Name?\")\n",
        "    Brand_Name = input(\"Customer: \")\n",
        "    write_to_text.write(\"Customer: \"+ Brand_Name + \" \\n \")\n",
        "\n",
        "    write_to_text.write(\"Chatbot: How Many Trucks in \" + Brand_Name + \"? (IN NUMBER)\" + \" \\n \")\n",
        "    print(\"Chatbot: How Many Trucks in \" + Brand_Name + \"? (IN NUMBER)\")\n",
        "    C_input = input(\"Customer: \")\n",
        "    write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "    Truck_Quantity = Ask_Question(\"Chatbot: How Many Trucks in \" + Brand_Name + \" (IN NUMBER only)\", C_input)\n",
        "\n",
        "    write_to_text.write(\"Chatbot: Are They of the same Model?[Yes/No]\" + \" \\n \")\n",
        "    print(\"Chatbot: Are They of the same Model?[Yes/No]\")\n",
        "    C_input = input(\"Customer: \")\n",
        "    write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "\n",
        "    if (\"no\" in C_input):\n",
        "        j = 1\n",
        "        while (j <= Truck_Quantity):\n",
        "            if (j == 1):\n",
        "                write_to_text.write(\"Chatbot: what is the 1st Truck model?\" + \" \\n \")\n",
        "                print(\"Chatbot: what is the 1st Truck model?\")\n",
        "                C_input = input(\"Customer: \")\n",
        "                write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "            elif (j == 2):\n",
        "                write_to_text.write(\"Chatbot: what is the 2nd Truck model?\" + \" \\n \")\n",
        "                print(\"Chatbot: what is the 2nd Truck model?\")\n",
        "                C_input = input(\"Customer: \")\n",
        "                write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "            elif (j == 3):\n",
        "                write_to_text.write(\"Chatbot: what is the 3nrd Truck model?\" + \" \\n \")\n",
        "                print(\"Chatbot: what is the 3nrd Truck model?\")\n",
        "                C_input = input(\"Customer: \")\n",
        "                write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "            elif (i > 3):\n",
        "                write_to_text.write(\"Chatbot: what is the \" + str(j) + \"th Truck model?\" + \" \\n \")\n",
        "                print(\"Chatbot: what is the \" + str(j) + \"th Truck model?\")\n",
        "                C_input = input(\"Customer: \")\n",
        "                write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "            j = j + 1\n",
        "    else:\n",
        "        write_to_text.write(\"Chatbot: What model are they?\" + \" \\n \")\n",
        "        print(\"Chatbot: What model are they?\")\n",
        "        C_input = input(\"Customer: \")\n",
        "        write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "\n",
        "#Starting Point of the Program\n",
        "write_to_text.write(\"Chatbot: Hello, Your Full Name Please \" + \" \\n \")\n",
        "print(\"Chatbot: Hello, Your Full Name Please\")\n",
        "Customer_Name = input(\"Customer: \")\n",
        "write_to_text.write(\"Customer: \" + Customer_Name + \" \\n \")\n",
        "\n",
        "write_to_text.write(\"Chatbot: Hi \" + Customer_Name + \" what\\'s the name of your company?\" + \" \\n \")\n",
        "print(\"Chatbot: Hi \" + Customer_Name + \" what\\'s the name of your company?\")\n",
        "C_input = input(\"Customer: \")\n",
        "write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "\n",
        "write_to_text.write(\"Chatbot: Do you own Trucks?[Yes/No]\" + \" \\n \")\n",
        "print(\"Chatbot: Do you own Trucks?[Yes/No]\")\n",
        "C_input = input(\"Customer: \")\n",
        "write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "if(\"no\" in C_input.lower()):\n",
        "    write_to_text.write(\"Please contact to one of our Colleague For more information \"+ \" \\n \")\n",
        "    print('Please contact to one of our colleague for more information ')\n",
        "    write_to_text.close()\n",
        "    sys.exit()\n",
        "\n",
        "write_to_text.write(\"Chatbot: How many truck's brand do you have? (IN NUMBER)\" + \" \\n \")\n",
        "print(\"Chatbot: How many truck's brand do you have? (IN NUMBER)\")\n",
        "C_input = input(\"Customer: \")\n",
        "write_to_text.write(\"Customer: \" + C_input + \" \\n \")\n",
        "Brand_Quantity = Ask_Question(\"Chatbot: How many truck's brand do you have? (IN NUMBER only)\", C_input)\n",
        "\n",
        "i = 1\n",
        "while i <= Brand_Quantity:\n",
        "    if (i == 1):\n",
        "        Truck_Information(\"1st\")\n",
        "    elif (i == 2):\n",
        "        Truck_Information(\"2nd\")\n",
        "    elif (i == 3):\n",
        "        Truck_Information(\"3rd\")\n",
        "    elif (i > 3):\n",
        "        Truck_Information(str(i)+\"th\")\n",
        "    i = i + 1\n",
        "\n",
        "print(\"Chatbot: Thank you very much for your information \\n we are now processing your information and \\n we will get back to you soon\\n until than have a nice day Bye:) \")\n",
        "write_to_text.write(\"Chatbot: Thank you very much for your information \\n we are now processing your information and \\n we will get back to you soon\\n until than have a nice day Bye:)  \\n \")\n",
        "write_to_text.close()\n"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Chatbot: Hello, Your Full Name Please\n",
            "Customer: Umer\n",
            "Chatbot: Hi Umer what's the name of your company?\n",
            "Customer: Tracks\n",
            "Chatbot: Do you own Trucks?[Yes/No]\n",
            "Customer: no\n",
            "Please contact to one of our colleague for more information \n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "SystemExit",
          "evalue": "ignored",
          "traceback": [
            "An exception has occurred, use %tb to see the full traceback.\n",
            "\u001b[0;31mSystemExit\u001b[0m\n"
          ]
        },
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.6/dist-packages/IPython/core/interactiveshell.py:2890: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
            "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
          ],
          "name": "stderr"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uYkNdakwWf71",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}