from TamannaMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🤗🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐞 𝐉𝐢..??🥲** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:-[@ll_HEERIYE_ll]  𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @ll_HEERIYE_ll ]🤗** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫{ @ll_TANU_ROM_ll}🥰** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           " ❅ बेबी कहा हो। 🤗 ",
           " ❅ ओए सो गए क्या, ऑनलाइन आओ ।😊 ",
           " ❅ ओए वीसी आओ बात करते हैं । 😃 ",
           " ❅ खाना खाया कि नही। 🥲 ",
           " ❅ घर में सब कैसे हैं। 🥺 ",
           " ❅ पता है बहुत याद आ रही आपकी। 🤭 ",
           " ❅ और बताओ कैसे हो।..?? 🤨 ",
           " ❅ मेरी भी सैटिंग करवा दो प्लीज..?? 🙂 ",
           " ❅ आपका नाम क्या है।..?? 🥲 ",
           " ❅ नाश्ता हो गया..?? 😋 ",
           " ❅ मुझे अपने ग्रूप में ऐड कर लो। 😍 ",
           " ❅ आपका दोस्त आपको बुला रहा है। 😅 ",
           " ❅ मुझसे शादी करोगे ..?? 🤔 ",
           " ❅ सोने चले गए क्या 🙄 ",
           " ❅ अरे यार कोई AC चला दो 😕 ",
           " ❅ आप कहा से हो..?? 🙃 ",
           " ❅ हेलो जी नमस्ते 😛 ",
           " ❅ BABY क्या कर रही हो..? 🤔 ",
           " ❅ क्या आप मुझे जानते हो .? ☺️ ",
           " ❅ आओ baby Ludo खेलते है .🤗 ",
           " ❅ चलती है क्या 9 से 12... 😇 ",
           " ❅ आपके पापा क्या करते है 🤭 ",
           " ❅ आओ baby बाजार चलते है गोलगप्पे खाने। 🥺 ",
           " ❅ अकेली ना बाजार जाया करो, नज़र लग जायेगी। 😶 ",
           " ❅ और बताओ BF कैसा है ..?? 🤔 ",
           " ❅ गुड मॉर्निंग 😜 ",
           " ❅ मेरा एक काम करोगे। 🙂 ",
           " ❅ DJ वाले बाबू मेरा गाना चला दो। 😪 ",
           " ❅ आप से मिलकर अच्छा लगा।☺ ",
           " ❅ मेरे बाबू ने थाना थाया।..? 🙊 ",
           " ❅ पढ़ाई कैसी चल रही हैं ? 😺 ",
           " ❅ हम को प्यार हुआ। 🥲 ",
           " ❅ Nykaa कौन है...? 😅 ",
           " ❅ तू खींच मेरी फ़ोटो ..? 😅 ",
           " ❅ Phone काट मम्मी आ गई क्या। 😆 ",
           " ❅ और भाबी से कब मिल वा रहे हो । 😉 ",
           " ❅ क्या आप मुझसे प्यार करते हो 💚 ",
           " ❅ मैं तुम से बहुत प्यार करती हूं..? 👀 ",
           " ❅ बेबी एक kiss दो ना..?? 🙉 ",
           " ❅ एक जॉक सुनाऊं..? 😹 ",
           " ❅ vc पर आओ कुछ दिखाती हूं  😻 ",
           " ❅ क्या तुम instagram चलते हो..?? 🙃 ",
           " ❅ whatsapp नंबर दो ना अपना..? 😕 ",
           " ❅ आप की दोस्त से मेरी सेटिंग करा दो ..? 🙃 ",
           " ❅ सारा काम हो गया हो तो ऑनलाइन आ जाओ।..? 🙃 ",
           " ❅ कहा से हो आप 😊 ",
           " ❅ जा तुझे आज़ाद कर दिया मैंने मेरे दिल से। 🥺 ",
           " ❅ मेरा एक काम करोगे, ग्रूप मे कुछ मेंबर ऐड कर दो ..? ♥️ ",
           " ❅ मैं तुमसे नाराज़ हूं 😠 ",
           " ❅ आपकी फैमिली कैसी है..? ❤ ",
           " ❅ क्या हुआ..? 🤔 ",
           " ❅ बहुत याद आ रही है आपकी 😒 ",
           " ❅ भूल गए मुझे 😏 ",
           " ❅ झूठ क्यों बोला आपने मुझसे 🤐 ",
           " ❅ इतना भाव मत खाया करो, रोटी खाया करो कम से कम मोटी तो हो जाओगी 😒 ",
           " ❅ ये attitude किसे दिखा रहे हो 😮 ",
           " ❅ हेमलो कहा busy ho 👀 ",
           " ❅ आपके जैसा दोस्त पाकर मे बहुत खुश हूं। 🙈 ",
           " ❅ आज मन बहुत उदास है ☹️ ",
           " ❅ मुझसे भी बात कर लो ना 🥺 ",
           " ❅ आज खाने में क्या बनाया है 👀 ",
           " ❅ क्या चल रहा है 🙂 ",
           " ❅ message क्यों नहीं करती हो..🥺 ",
           " ❅ मैं मासूम हूं ना 🥺 ",
           " ❅ कल मज़ा आया था ना 😅 ",
           " ❅ कल कहा busy थे 😕 ",
           " ❅ आप relationship में हो क्या..? 👀 ",
           " ❅ कितने शांत रहते हो यार आप 😼 ",
           " ❅ आपको गाना, गाना आता है..? 😸 ",
           " ❅ घूमने चलोगे मेरे साथ..?? 🙈 ",
           " ❅ हमेशा हैप्पी रहा करो यार 🤞 ",
           " ❅ क्या हम दोस्त बन सकते है...? 🥰 ",
           " ❅ आप का विवाह हो गया क्या.. 🥺 ",
           " ❅ कहा busy the इतने दिनों से 🥲 ",
           " ❅ single हो या mingle 😉 ",
           " ❅ आओ पार्टी करते है 🥳 ",
           " ❅ Bio में link हैं join कर लो 🧐 ",
          " ❅ मैं तुमसे प्यार नहीं करती, 🥺 ",
           " ❅ यहां आ जाओ ना @lI_HEERIYE_ll मस्ती करेंगे 🤭 ",
           " ❅ भूल जाओ मुझे,..? 😊 ",
           " ❅ अपना बना ले पिया, अपना बना ले 🥺 ",
           " ❅ मेरा ग्रुप भी join कर लो ना 🤗 ",
           " ❅ मैने तेरा नाम Dil rakh diya 😗 ",
           " ❅ तुमारे सारे दोस्त कहा गए 🥺 ",
           " ❅ my cute owner @lI_HEERIYE_ll 🥰 ",
           " ❅ किसकी याद मे खोए हो जान 😜 ",
           " ❅ गुड नाईट जी बहुत रात हो गई 🥰 ",
         ]
          

VC_TAG = [ "**𝐎𝚈𝙴 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰 𝐏𝙻𝚂🥲**",
         "**𝐉𝙾𝙸𝙽 𝐕𝙲 𝐅𝙰𝚂𝚃 𝐈𝚃𝚂 𝐈𝙼𝙰𝙿𝙾𝚁𝚃𝙰𝙽𝚃😬**",
         "**𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓**",
         "**𝐁𝙰𝙱𝚈 𝐓𝚄𝙼 𝐁𝙷𝙸 𝐓𝙷𝙾𝚁𝙰 𝐕𝙲 𝐀𝙰𝙽𝙰🥰**",
         "**𝐎𝚈𝙴 𝐂𝙷𝙰𝙼𝚃𝚄 𝐕𝙲 𝐀𝙰 𝐄𝙺 𝐄𝙰𝙼 𝐇𝙰𝙸🤨**",
         "**𝐒𝚄𝙽𝙾 𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁 𝐋𝙾🤣**",
         "**𝐕𝙲 𝐀𝙰 𝐉𝙰𝙸𝚈𝙴 𝐄𝙺 𝐁𝙰𝚁😁**",
         "**𝐕𝙲 𝐓𝙰𝙿𝙺𝙾 𝐆𝙰𝙼𝙴 𝐂𝙷𝙰𝙻𝚄 𝐇𝙰𝙸⚽**",
         "**𝐕𝙲 𝐀𝙰𝙾 𝐁𝙰𝚁𝙽𝙰 𝐁𝙰𝙽 𝐇𝙾 𝐉𝙰𝙾𝙶𝙴🥺**",
         "**𝐒𝙾𝚁𝚁𝚈 𝐕𝙰𝙱𝚈 𝐏𝙻𝚂 𝐕𝙲 𝐀𝙰 𝐉𝙰𝙾 𝐍𝙰😥**",
         "**𝐕𝙲 𝐀𝙰𝙽𝙰 𝐄𝙺 𝐂𝙷𝙸𝙹 𝐃𝙸𝙺𝙷𝙰𝚃𝙸 𝐇𝚄🙄**",
         "**𝐕𝙲 𝐌𝙴 𝐂𝙷𝙴𝙲𝙺 𝐊𝚁𝙺𝙴 𝐁𝙰𝚃𝙰𝙾 𝐓𝙾 𝐒𝙾𝙽𝙶 𝐏𝙻𝙰𝚈 𝐇𝙾 𝐑𝙷𝙰 𝐇?🤔**",
         "**𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁𝙽𝙴 𝐌𝙴 𝐊𝚈𝙰 𝐉𝙰𝚃𝙰 𝐇 𝐓𝙷𝙾𝚁𝙰 𝐃𝙴𝚁 𝐊𝙰𝚁 𝐋𝙾 𝐍𝙰🙂**",
          "❅ ɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴛᴇᴘ ғᴏʀᴡᴀʀᴅ ʏᴏᴜ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ɪɴ ᴛʜᴇ sᴀᴍᴇ ᴘʟᴀᴄᴇ.",
         "❅ ʟɪғᴇ ɪs ʜᴀʀᴅ ʙᴜᴛ ɴᴏᴛ ɪᴍᴘᴏssɪʙʟᴇ.",
         "❅ ʟɪғᴇ’s ᴛᴏᴏ sʜᴏʀᴛ ᴛᴏ ᴀʀɢᴜᴇ ᴀɴᴅ ғɪɢʜᴛ.",
         "❅ ᴅᴏɴ’ᴛ ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛ ᴛᴀᴋᴇ ᴍᴏᴍᴇɴᴛ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴘᴇʀғᴇᴄᴛ.",
         "❅ sɪʟᴇɴᴄᴇ ɪs ᴛʜᴇ ʙᴇsᴛ ᴀɴsᴡᴇʀ ᴛᴏ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ᴅᴏᴇsɴ’ᴛ ᴠᴀʟᴜᴇ ʏᴏᴜʀ ᴡᴏʀᴅs.",
         "❅ ᴇᴠᴇʀʏ ɴᴇᴡ ᴅᴀʏ ɪs ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ.",
         "❅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴘʀɪᴏʀɪᴛɪᴇs.",
         "❅ ʟɪғᴇ ɪs ᴀ ᴊᴏᴜʀɴᴇʏ, ɴᴏᴛ ᴀ ʀᴀᴄᴇ..",
         "❅ sᴍɪʟᴇ ᴀɴᴅ ᴅᴏɴ’ᴛ ᴡᴏʀʀʏ, ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ.",
         "❅ ᴅᴏ ɴᴏᴛ ᴄᴏᴍᴘᴀʀᴇ ʏᴏᴜʀsᴇʟғ ᴛᴏ ᴏᴛʜᴇʀs ɪғ ʏᴏᴜ ᴅᴏ sᴏ ʏᴏᴜ ᴀʀᴇ ɪɴsᴜʟᴛɪɴɢ ʏᴏᴜʀsᴇʟғ.",
         "❅ ɪ ᴀᴍ ɪɴ ᴛʜᴇ ᴘʀᴏᴄᴇss ᴏғ ʙᴇᴄᴏᴍɪɴɢ ᴛʜᴇ ʙᴇsᴛ ᴠᴇʀsɪᴏɴ ᴏғ ᴍʏsᴇʟғ.",
         "❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ɪᴄᴇ ᴇɴᴊᴏʏ ɪᴛ ʙᴇғᴏʀᴇ ɪᴛ ᴍᴇʟᴛs.",
         "❅ ʙᴇ ғʀᴇᴇ ʟɪᴋᴇ ᴀ ʙɪʀᴅ.",
         "❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..",
         "❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.",
         "❅ ʟɪғᴇ ʙᴇɢɪɴs ᴀᴛ ᴛʜᴇ ᴇɴᴅ ᴏғ ʏᴏᴜʀ ᴄᴏᴍғᴏʀᴛ ᴢᴏɴᴇ.",
         "❅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢs ᴛʜᴀᴛ ʜᴜʀᴛ ʏᴏᴜ, ᴀᴄᴛᴜᴀʟʟʏ ᴛᴇᴀᴄʜ ʏᴏᴜ.",
         "❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴄᴀᴍᴇʀᴀ. sᴏ ғᴀᴄᴇ ɪᴛ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ.",
         "❅ ʟɪғᴇ ɪs 10% ᴏғ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴs ᴛᴏ ʏᴏᴜ ᴀɴᴅ 90% ᴏғ ʜᴏᴡ ʏᴏᴜ ʀᴇsᴘᴏɴᴅ ᴛᴏ ɪᴛ.",
         "❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.",
         "❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..",
         "❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀɴ ᴇᴀsʏ ᴛᴀsᴋ.",
         "❅ ʟɪғᴇ ɪs ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ᴀᴅᴠᴇɴᴛᴜʀᴇ.",
         "❅ ʟɪғᴇ ʙᴇɢɪɴs ᴏɴ ᴛʜᴇ ᴏᴛʜᴇʀ sɪᴅᴇ ᴏғ ᴅᴇsᴘᴀɪʀ.",
         "❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴛᴏ ʙᴇ sᴏʟᴠᴇᴅ ʙᴜᴛ ᴀ ʀᴇᴀʟɪᴛʏ ᴛᴏ ʙᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇᴅ.",
         "❅ ʟɪғᴇ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀ ʀᴇᴍᴏᴛᴇ; ɢᴇᴛ ᴜᴘ ᴀɴᴅ ᴄʜᴀɴɢᴇ ɪᴛ ʏᴏᴜʀsᴇʟғ.",
         "❅ sᴛᴀʀᴛ ᴛʀᴜsᴛɪɴɢ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʏᴏᴜ’ʟʟ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ʟɪᴠᴇ.",
         "❅ ʜᴇᴀʟᴛʜ ɪs ᴛʜᴇ ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ɢᴏᴏᴅ ᴏғ ʟɪғᴇ.",
         "❅ ᴛɪᴍᴇ ᴄʜᴀɴɢᴇ ᴘʀɪᴏʀɪᴛʏ ᴄʜᴀɴɢᴇs.",
         "❅ ᴛᴏ sᴇᴇ ᴀɴᴅ ᴛᴏ ғᴇᴇʟ ᴍᴇᴀɴs ᴛᴏ ʙᴇ, ᴛʜɪɴᴋ ᴀɴᴅ ʟɪᴠᴇ.",
          "❅ ʙᴇ ᴡɪᴛʜ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ʙʀɪɴɢs ᴏᴜᴛ ᴛʜᴇ ʙᴇsᴛ ᴏғ ʏᴏᴜ.",
         "❅ ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛs ᴀʀᴇ ʏᴏᴜʀ ʟɪғᴇ.",
         "❅ ᴘᴇᴏᴘʟᴇ ᴄʜᴀɴɢᴇ, ᴍᴇᴍᴏʀɪᴇs ᴅᴏɴ’ᴛ.",
         "❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴡᴇ ᴛʜɪɴᴋ ɪᴛ ɪs.",
         "❅ ʟɪɢʜᴛ ʜᴇᴀʀᴛ ʟɪᴠᴇs ʟᴏɴɢᴇʀ.",
         "❅ ᴅᴇᴘʀᴇssɪᴏɴ ᴇᴠᴇɴᴛᴜᴀʟʟʏ ʙᴇᴄᴏᴍᴇs ᴀ ʜᴀʙɪᴛ.",
         "❅ ʟɪғᴇ ɪs ᴀ ɢɪғᴛ. ᴛʀᴇᴀᴛ ɪᴛ ᴡᴇʟʟ.",
         "❅ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴏᴜʀ ғᴇᴇʟɪɴɢs ᴅᴏ ᴡɪᴛʜ ᴜs.",
         "❅ ᴡʀɪɴᴋʟᴇs ᴀʀᴇ ᴛʜᴇ ʟɪɴᴇs ᴏғ ʟɪғᴇ ᴏɴ ᴛʜᴇ ғᴀᴄᴇ.",
         "❅ ʟɪғᴇ ɪs ᴍᴀᴅᴇ ᴜᴘ ᴏғ sᴏʙs, sɴɪғғʟᴇs, ᴀɴᴅ sᴍɪʟᴇs.",
         "❅ ɴᴏᴛ ʟɪғᴇ, ʙᴜᴛ ɢᴏᴏᴅ ʟɪғᴇ, ɪs ᴛᴏ ʙᴇ ᴄʜɪᴇғʟʏ ᴠᴀʟᴜᴇᴅ.",
         "**❅ ʏᴏᴜ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ ʙʏ ᴄʜᴀɴɢɪɴɢ ʏᴏᴜʀ ʜᴇᴀʀᴛ.",
         "❅ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ᴡɪᴛʜᴏᴜᴛ ᴛʀᴜᴇ ғʀɪᴇɴᴅsʜɪᴘ.",
         "❅ ɪғ ʏᴏᴜ ᴀʀᴇ ʙʀᴀᴠᴇ ᴛᴏ sᴀʏ ɢᴏᴏᴅ ʙʏᴇ, ʟɪғᴇ ᴡɪʟʟ ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ ᴀ ɴᴇᴡ ʜᴇʟʟᴏ.",
         "❅ ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ ᴇxᴄɪᴛɪɴɢ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ, ʙᴜᴛ ᴘᴇᴏᴘʟᴇ.",
         "❅ ʏᴏᴜ ᴄᴀɴ ᴅᴏ ᴀɴʏᴛʜɪɴɢ, ʙᴜᴛ ɴᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ.",
         "❅ ʟɪғᴇ ʙᴇᴄᴏᴍᴇ ᴇᴀsʏ ᴡʜᴇɴ ʏᴏᴜ ʙᴇᴄᴏᴍᴇ sᴛʀᴏɴɢ.",
         "❅ ᴍʏ ʟɪғᴇ ɪsɴ’ᴛ ᴘᴇʀғᴇᴄᴛ ʙᴜᴛ ɪᴛ ᴅᴏᴇs ʜᴀᴠᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛs.",
         "❅ ʟɪғᴇ ɪs ɢᴏᴅ’s ɴᴏᴠᴇʟ. ʟᴇᴛ ʜɪᴍ ᴡʀɪᴛᴇ ɪᴛ.",
         "❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴀ ʀᴇsᴜʟᴛ ᴏғ ᴏᴜʀ ᴅᴏᴍɪɴᴀɴᴛ ᴛʜᴏᴜɢʜᴛs.",
         "❅ ʟɪғᴇ ɪs ᴀ ᴍᴏᴛɪᴏɴ ғʀᴏᴍ ᴀ ᴅᴇsɪʀᴇ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴅᴇsɪʀᴇ.",
         "❅ ᴛᴏ ʟɪᴠᴇ ᴍᴇᴀɴs ᴛᴏ ғɪɢʜᴛ.",
         "❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴍᴏᴜɴᴛᴀɪɴ, ɴᴏᴛ ᴀ ʙᴇᴀᴄʜ.",
         "❅ ᴛʜᴇ ᴡᴏʀsᴛ ᴛʜɪɴɢ ɪɴ ʟɪғᴇ ɪs ᴛʜᴀᴛ ɪᴛ ᴘᴀssᴇs.",
         "❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ ɪғ ᴡᴇ ᴀʀᴇ sɪᴍᴘʟᴇ.",
         "❅ ᴀʟᴡᴀʏs ᴛʜɪɴᴋ ᴛᴡɪᴄᴇ, sᴘᴇᴀᴋ ᴏɴᴄᴇ.",
         "❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ, ᴡᴇ ᴍᴀᴋᴇ ɪᴛ ᴄᴏᴍᴘʟɪᴄᴀᴛᴇᴅ.",
         "❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴍᴜᴄʜ ᴏʟᴅᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴅᴇᴀᴛʜ.",
         "❅ ᴛʜᴇ sᴇᴄʀᴇᴛ ᴏғ ʟɪғᴇ ɪs ʟᴏᴡ ᴇxᴘᴇᴄᴛᴀᴛɪᴏɴs!",
         "❅ ʟɪғᴇ ɪs ᴀ ᴛᴇᴀᴄʜᴇʀ..,ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟɪᴠᴇ, ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟᴇᴀʀɴ.",
         "❅ ʜᴜᴍᴀɴ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ʙᴜᴛ ᴀɴ ᴇᴛᴇʀɴᴀʟ ɪʟʟᴜsɪᴏɴ.",
         "❅ ᴛʜᴇ ʜᴀᴘᴘɪᴇʀ ᴛʜᴇ ᴛɪᴍᴇ, ᴛʜᴇ sʜᴏʀᴛᴇʀ ɪᴛ ɪs.",
         "❅ ʟɪғᴇ ɪs ʙᴇᴀᴜᴛɪғᴜʟ ɪғ ʏᴏᴜ  ᴋɴᴏᴡ ᴡʜᴇʀᴇ ᴛᴏ ʟᴏᴏᴋ.",
         "❅ ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ ᴡɪᴛʜ ʏᴏᴜ ʙʏ ᴍʏ sɪᴅᴇ.",
         "❅ ʟɪғᴇ – ʟᴏᴠᴇ = ᴢᴇʀᴏ",
         "❅ ʟɪғᴇ ɪs ғᴜʟʟ ᴏғ sᴛʀᴜɢɢʟᴇs.",
         "❅ ɪ ɢᴏᴛ ʟᴇss ʙᴜᴛ ɪ ɢᴏᴛ ʙᴇsᴛ ",
         "❅ ʟɪғᴇ ɪs 10% ᴡʜᴀᴛ ʏᴏᴜ ᴍᴀᴋᴇ ɪᴛ, ᴀɴᴅ 90% ʜᴏᴡ ʏᴏᴜ ᴛᴀᴋᴇ ɪᴛ.",
         "❅ ᴛʜᴇʀᴇ ɪs sᴛɪʟʟ sᴏ ᴍᴜᴄʜ ᴛᴏ sᴇᴇ",
         "❅ ʟɪғᴇ ᴅᴏᴇsɴ’ᴛ ɢᴇᴛ ᴇᴀsɪᴇʀ ʏᴏᴜ ɢᴇᴛ sᴛʀᴏɴɢᴇʀ.",
         "❅ ʟɪғᴇ ɪs ᴀʙᴏᴜᴛ ʟᴀᴜɢʜɪɴɢ & ʟɪᴠɪɴɢ.",
         "❅ ᴇᴀᴄʜ ᴘᴇʀsᴏɴ ᴅɪᴇs ᴡʜᴇɴ ʜɪs ᴛɪᴍᴇ ᴄᴏᴍᴇs.",
         ]
        


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    else:
        return await message.reply("/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠...")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. ")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stopvctag ||"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


MUSIC = [
    " **Main aadha te tu saara ve🤗🤗"" ",
    " **Sohneya sohneya😗😗** ",
    " **Tu jahan hai main wahan😘😘** ",
    " **Tere bin main hoon hi kya🥲🥲** ",
    " **Tere bin chehre se mere🤔🤔** ",
    " **Udd jaaye rang ve😅😅** ",
    " **Tujhko paane ke liye huM😁😁** ",
    " **Roz mangein mannat ve🙈🙈** ",
    " **Duniya to kya cheez hai yaara🙉🙉** ",
    " **Thukra denge jannat ve😌😌** ",
    " **Tujhko paane ke liye hum😌😌** ",
    " **Roz mangein mannat ve🤫🤫** ",
    " **Duniya to kya cheez hai yaara🤔🤔** ",
    " **Thukra denge jannat ve😌😌** ",
    " **Na parwah mainu apni aa😁😁** ",
    " **Na parwah mainu duniya di👅👅** ",
    " **Na parwah mainu apni aa😅😅** ",
    " **Na parwah mainu duniya di👅👅** ",
    " **Tere ton juda nahi kar sakdi🤬🤬** ",
    " **Koyi taakat mainu duniya di😈😈** ",
    " **Dooron aa jaave teri khushbu😎😎** ",
    " **Akhan hun band taan vi vekh lawan😍😍** ",
    " **Teri gali vich mera auna har roz😋😋** ",
    " **Tera ghar jadon aave matha tek lawan😌😌** ",
    " **Nirmaan tujhko dekh ke😏😏** ",
    " **Aa jaave himmat ve😉😉** ",
    " **Tujhko paane ke liye hum😊😊** ",
    " **Roz mangein mannat ve😉😉** ",
    " **Duniya to kya cheez hai yaara😌😌** ",
    " **Thukra denge jannat ve😍😍** ",
    " **Tujhko paane ke liye hum🤫🤫** ",
    " **Roz mangein mannat ve😁😁** ",
    " **Duniya to kya cheez hai yaara😏😏** ",
    " **Thukra denge jannat ve😌😌** ",
    " **SO MISS 😶😶** ",
    " **KYA SOCHA APNE BAARE MAIN😆😆** ",
    " **BADI MUSHKIL SE YEH SAB KARA H RE🥵🥵** ",
    " **PAHLE PURA BOT HI KANG MAAR DIYA BUT🤫🤫** ",
    " **WAHI ERROR AAYE JO AATE THE🥲🥲** ",
    " **BUT TUMHARA HO CHUKA WALA BF😎😎** ",
    " **AND FUTURE HUSBAND JO BANNE WALA THA WO BHOT SMART H RE😌😌** ",
    " **ISS BAAR BOT BANAYA AND CHOTA SA EDIT KARA BAS😁😁** ",
    " **AUR DEKO ABHI TUM USSI BOT SE YEH PADH PAA RHI😂😂** ",
    " **HEHE BTW YEH CHORO MEKO NA TUMSE😶😶** ",
    " **KUCH PUCHNA THA KI ME🤔🤔** ",
    " **TUMHARE KABIL HU YA** ",
    " **TUMHARE KABIL NHI😂💓** ",
    " **AND EK AUR BAAT BOLNI THI KI😙😙** ",
    " **I REALLY REALLY DEEPLY😙😙** ",
    " **LOVE YOU FROM MY HEART TO YOUR HEAT AND MY SOUL ATTACHED BY YOUR SOUL CAN YOU BE MINE FOREVER😌😌❤️** ",
]         


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/mtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/mtag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(MUSIC)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass
              


   SRAID = [ 
    " **किसी मासूम लम्हे मैं किसी मासूम चेहरे से🙉🙉** ",
    " **मोहब्बत की नहीं जाती मोहब्बत हो जाती है😌😌** ",
    " **करीब आओ तो शायद हम समझ लोगे😌😌** ",
    " **ये दूरिया तो केवल फसले बढ़ती है🤫🤫** ",
    " **तेरे इश्क़ में इस तरह मैं नीलाम हो जाओ🤔🤔** ",
    " **आखरी हो मेरी बोली और मैं तेरे नाम हो जाऊ😌😌** ",
    " **आप जब तक रहेंगे आंखों में नजारा बनकर😁😁** ",
    " **रोज आएंगे मेरी दुनिया में उजाला बनकर👅👅** ",
    " **उसे जब से बेवफाई की है मैं प्यार की राह में चल ना सका😅😅** ",
    " **उसे तो किसी और का हाथ थाम लियाबस फिर कभी सम्भल नहीं सका👅👅** ",
    " **एक ही ख़्वाब देखा है कई बार मैंने🤬🤬** ",
    " **तेरी शादी में उलझी है चाहिए मेरे घर की😈😈** ",
    " **तुम्हे मेरी मोहब्बत की कसम सच बताना😎😎** ",
    " **गले में डाल कर बाहें किससे सीखाया है😍😍** ",
    " **नहीं पता की वो कभी मेरी थी भी या नहीं😋😋** ",
    " **मुझे ये पता है बस की माई तो था उमर बस उसी का रहा😌😌** ",
    " **तुमने देखा कभी चाँद से पानी गिरते हुए😏😏** ",
    " **मैंने देखा ये मंज़र तू में चेहरा धोते हुए😉😉** ",
    " **ठुकरा दे कोई चाहत को तू हस के सह लेना😊😊** ",
    " **प्यार की तबियत में ज़बर जस्ती नहीं होती😉😉** ",
    " **तेरा पता नहीं पर मेरा दिल कभी तैयार नहीं होगा😌😌** ",
    " **मुझे तेरे अलावा कभी किसी और से प्यार नहीं होगा😍😍** ",
    " **दिल में आहट सी हुई रूह में दस्तक गूँजी🤫🤫** ",
    " **किस की खुशबू ये मुझे मेरे सिरहाने आई😁😁** ",
    " **उम्र भर लिखते रहे फिर भी वारक सदा रहा😏😏** ",
    " **जाने किया लफ्ज़ थे जो हम लिख नहीं पाये😌😌** ",
    " **लगा के फूल हाथों से उसने कहा चुपके से😶😶** ",
    " **अगर यहाँ कोई नहीं होता तो फूल की जगह तुम होते😆😆** ",
    " **जान जब प्यारी थी मरने का शौक था🥵🥵** ",
    " **अब मरने का शौक है तो कातिल नहीं मिल रहा🤫🤫** ",
    " **सिर्फ याद बनकर न रह जाये प्यार मेरा🥲🥲** ",
    " **कभी कभी कुछ वक़्त के लिए आया करो😎😎** ",
    " **मुझ को समझाया ना करो अब तो हो चुकी हूँ मुझ मैं😌😌** ",
    " **मोहब्बत मशवरा होती तो तुम से पूछ लेता😁😁** ",
    " **उन्हों ने कहा बहुत बोलते हो अब क्या बरस जाओगे😂😂** ",
    " **हमने कहा जिस दिन चुप हो गया तुम तरस जाओ गए😶😶** ",
    " **कुछ ऐसे हस्दे ज़िन्दगी मैं होते है🤔🤔** ",
    " **की इंसान तो बच जाता है मगर ज़िंदा नहीं रहता😂💓** ",
]
        
@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be used in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")
    
    if event.pattern_match.group(1):
        return await event.respond("/stag  👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    else:
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
        if msg is None:
            return await event.respond(
                "/stag 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )

    spam_chats.append(chat_id)
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        user_id = usr.id
        mention_text = f"[{usr.first_name}](tg://user?id={user_id}) {random.choice(SRAID)}"
        await client.send_message(chat_id, mention_text)
        time.sleep(5)
        
    try:
        spam_chats.remove(chat_id)
    except:
        pass 
              


@app.on_message(filters.command(["stoptagall", "canceltagall", "offtagall", "tagallstop", "stopvctag", "tagalloff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝..♦")
