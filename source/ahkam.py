import random
from pyrogram import Client, filters, idle
from pyrogram import Client 
from source.info import (joinch)
from pyrogram.types import Message
from pyrogram import enums

ahkam =  ["  صورة وجهك او رجلك او خشمك او يدك ؟ ",
"  اصدر اي صوت يطلبه منك الاعبين ؟ ",
"  سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
"  روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
"  قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
"  سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
"  ذي المرة لك لا تعيدها ؟ ",
"  ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
"  صور اي شيء يطلبه منك الاعبين ؟ ",
"  اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
"  سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
"  اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
"  ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
"  روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
"  اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
"  قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
"  سامحتك خلاص مافيه عقاب لك  ؟ ",
"  اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
"  غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
"  اتصل على امك و قول لها انك تحبها  ؟ ",
"  لا يوجد سؤال لك سامحتك  ؟ ",
"  قل لواحد ماتعرفه عطني كف ؟ ",
"  منشن الجميع وقل انا اكرهكم ؟ ",
"  اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
"  روح المطبخ و اكسر صحن  ؟ ",
"  اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
"  قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
"  تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
"  لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
"  قول قصيدة  ؟ ",
"  تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
"  اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
"  اول واحد تشوفه عطه كف ؟ ",
"  سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
"  سامحتك خلاص مافيه عقاب لك  ؟ ",
"  اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
"  روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
"  تاخذ عقابين ؟ ",
"  قول اسم امك افتخر بأسم امك ؟ ",
"  ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
"  اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
"  اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
"  تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
"  تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
"  اتصل على الوالدهو تقول لهااحب وحده ؟ ",
"  تتصل على شرطي تقول له عندكم مطافي ؟ ",
"  خلاص سامحتك ؟ ",
"  تصيح في الشارع انامجنوون ؟ ",
"  تروح عند شخص وقول له احبك ؟"]

@Client.on_message(filters.command(["حكم", "احكام"], ""))
async def bott9(client: Client, message: Message):
    if not message.chat.type == enums.ChatType.PRIVATE:
      if await joinch(message):
            return
    bar = random.choice(ahkam)
    await message.reply_text(f"**{bar}؟**", disable_web_page_preview=True)