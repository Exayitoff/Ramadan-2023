from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


keyboard = InlineKeyboardMarkup(row_width=2)

button1 = InlineKeyboardButton('Kechagi Taqvim 🌙 ', callback_data='kecha')
button2 = InlineKeyboardButton('Bugungi Taqvim 🌙 ', callback_data='bugun')
button3 = InlineKeyboardButton('Ertangi Taqvim 🌙 ', callback_data='ertaga')

keyboard.row(button1,button3)
keyboard.add(button2)





ramadan = [
    {
      "kun":"1",
      "Saharlik": "05:19",
      "Iftorlik": "19:25"
    },
    {
      "kun":"2",
      "Saharlik": "05:17",
      "Iftorlik": "19:26"
    }
    ,
    {
      "kun":"3",
      "Saharlik": "05:15",
      "Iftorlik": "9:28"
    }
    ,
    {
      "kun":"4",
      "Saharlik": "05:14",
      "Iftorlik": "19:29"
    }
    ,
    {
      "kun":"5",
      "Saharlik": "05:12",
      "Iftorlik": "19:30"
    }
    ,
    {
      "kun":"6",
      "Saharlik": "05:10",
      "Iftorlik": "19:31"
    }
    ,
    {
      "kun":"7",
      "Saharlik": "05:08",
      "Iftorlik": "19:32"
    }
    ,
    {
      "kun":"8",
      "Saharlik": "05:06",
      "Iftorlik": "19:33"
    }
    ,
    {
      "kun":"9",
      "Saharlik": "05:04",
      "Iftorlik": "19:34"
    }
    ,
    {
      "kun":"10",
      "Saharlik": "05:00",
      "Iftorlik": "19:36"
    }
    ,
    {
      "kun":"11",
      "Saharlik": "04:58",
      "Iftorlik": "19:37"
    }
    ,
    {
      "kun":"12",
      "Saharlik": "04:57",
      "Iftorlik": "19:38"
    }
    ,
    {
      "kun":"13",
      "Saharlik": "04:55",
      "Iftorlik": "19:39"
    }
    ,
    {
      "kun":"14",
      "Saharlik": "04:53",
      "Iftorlik": "19:40"
    }
    ,
    {
      "kun":"15",
      "Saharlik": "04:51",
      "Iftorlik": "19:41"
    }
    ,
    {
      "kun":"16",
      "Saharlik": "04:49",
      "Iftorlik": "19:42"
    }
      ,
    {
      "kun":"17",
      "Saharlik": "04:47",
      "Iftorlik": "19:44"
    }
      ,
    {
      "kun":"18",
      "Saharlik": "04:45",
      "Iftorlik": "19:45"
    }
      ,
    {
      "kun":"19",
      "Saharlik": "04:43",
      "Iftorlik": "19:46"
    }
      ,
    {
      "kun":"20",
      "Saharlik": "04:41",
      "Iftorlik": "19:48"
    }
      ,
    {
      "kun":"21",
      "Saharlik": "04:40",
      "Iftorlik": "19:49"
    }
  ]
