'''
const songs = document.querySelectorAll('ytmusic-responsive-list-item-renderer');

// Check if any songs were found
if (songs.length === 0) {
    console.error('No songs found
check the selector or page structure.');
} else {
    const songData = [];

    // Loop through each song container
    songs.forEach(song => {
        // Extracting the title (song name)
        const title = song.querySelector('.title-column a')?.textContent.trim() || 'No Title';

        // Extracting the artist name (the <a> tag is inside a parent with class 'flex-column style-scope ytmusic-responsive-list-item-renderer complex-string')
        const artist = song.querySelector('.flex-column.style-scope.ytmusic-responsive-list-item-renderer.complex-string a.yt-simple-endpoint.style-scope.yt-formatted-string')?.textContent.trim() || 'No Artist';

        // Extracting the music URL (href of the song link)
        const musicUrl = song.querySelector('.title-column a')?.href || 'No URL';

        // Extracting the thumbnail image URL (if there's an image element)
        const thumbnail = song.querySelector('img')?.src || 'No Thumbnail';

        // Store the song data in the array
        songData.push({
            title,
            artist,
            musicUrl,
            thumbnail
        });
    });

    // Output the array of song data to the console
    console.log(songData);
}
'''

import yt_dlp
import os

musicData = [
    {
        'title': 'Mera Haal',
        'artist': 'Gurnam Bhullar',
        'musicUrl': 'https://music.youtube.com/watch?v=UeWvGAv_j7k&list=RDAMVMUeWvGAv_j7k',
        'thumbnail': "https://lh3.googleusercontent.com/j_bVlB27zS8xKQ5WAx2mODS2RR22vd4qPOxqRoSyNxry12rQUBATeqqURyAjCgZpU7FA-EIKw4EGCfhe=w120-h120-l90-rj"

    },
    {
        'title': 'Supne',
        'artist': 'Prabh Bains',
        'musicUrl': 'https://music.youtube.com/watch?v=VVXXFraolRE&list=RDAMVMVVXXFraolRE',
        'thumbnail': "https://lh3.googleusercontent.com/hzoauGz55aQH8e9zpGPWUvR-OxQrc_ZCH-FW2xK0rtLEgyvy7E3mK3ISJbyOiz4e67Q-5vbFBxtTnkdoRQ=w120-h120-l90-rj"

    },
    {
        'title': 'Jaat Da Muqabala',
        'artist': 'Sidhu Moosewala',
        'musicUrl': 'https://music.youtube.com/watch?v=6MS0oT7v-bI&list=RDAMVM6MS0oT7v-bI',
        'thumbnail': "https://lh3.googleusercontent.com/RDWYxn9Rlgqe4LQ9x22zUg99Q67M5p1h1MQP4pUk5leRmrxFKSbaUQF9Yg8rSn0QVP2v0XhmhU97XqaZ=w120-h120-l90-rj"

    },
    {
        'title': 'Mere Wala Sardar',
        'artist': 'Jugraj Sandhu',
        'musicUrl': 'https://music.youtube.com/watch?v=lyGcBsETYqU&list=RDAMVMlyGcBsETYqU',
        'thumbnail': "https://lh3.googleusercontent.com/YCi-g5m8D_ZHvVshB6jLewMUUsPy3ddic37-vvR-xKBlfWULIHSXXrfMe2JmGkbxiHNC3NIZYW6XJGN-=w120-h120-l90-rj"

    },
    {
        'title': 'Jhalle (feat. Gurnam Bhullar)',
        'artist': 'Music Machine',
        'musicUrl': 'https://music.youtube.com/watch?v=tAur9KK3XyY&list=RDAMVMtAur9KK3XyY',
        'thumbnail': "https://lh3.googleusercontent.com/6wRL28R-a4Mtns3rPe6diVgMlIvYpDM3Z4aZcZ0u0HgSD9QOLOn2PZjPAsUu_ijgtvZ48-kfKq6709PR=w120-h120-l90-rj"

    },
    {
        'title': 'Panjeban',
        'artist': 'Shivjot',
        'musicUrl': 'https://music.youtube.com/watch?v=VMjQoycq3Wc&list=RDAMVMVMjQoycq3Wc',
        'thumbnail': "https://lh3.googleusercontent.com/D-JEuim2jdr1uz5DJB8R_qAwOIfDZxERxF5Y3PjboWsufjboNb-NTJga9KlaG17GcvHuyBzukvZb-D6N=w120-h120-l90-rj"

    },
    {
        'title': 'Bille Bille Naina Waliye',
        'artist': 'Khan Bhaini',
        'musicUrl': 'https://music.youtube.com/watch?v=F9Ms-PFU5bM&list=RDAMVMF9Ms-PFU5bM',
        'thumbnail': "https://lh3.googleusercontent.com/2-fXxyr6S3RCA5_u7npgTpi28FRwJXw2giEbvZPk6x6GzrAooKXhc68Y7oGyr7_9tvSDtqK6ev0Pwr4=w120-h120-l90-rj"

    },
    {
        'title': 'Parshawan',
        'artist': 'Harnoor',
        'musicUrl': 'https://music.youtube.com/watch?v=c1kRdkq31XY&list=RDAMVMc1kRdkq31XY',
        'thumbnail': "https://lh3.googleusercontent.com/TPuvytisVK7GbCnQYFsWFsMRQOVipoFL8gSOYfHLPiw8B0aHpGEtKOlyb6qxntmDEebb6rOKaUFEhW73=w120-h120-l90-rj"

    },
    {
        'title': 'Struggler',
        'artist': 'R Nait',
        'musicUrl': 'https://music.youtube.com/watch?v=VqNx9RP49Mk&list=RDAMVMVqNx9RP49Mk',
        'thumbnail': "https://lh3.googleusercontent.com/wO0NcP6IiJJtwcfC_0x9OTdJx1i7gifj7xM625IP3nzz3lm1sojY-8-tHdqWINmDp-_gH46xVIpaxgKkjA=w120-h120-l90-rj",

    },
    {
        'title': 'Santan Di Tasveer',
        'artist': 'Dhadi Tarsem Singh Moranwali',
        'musicUrl': 'https://music.youtube.com/watch?v=-KqxoCdbzrc&list=RDAMVM-KqxoCdbzrc',
        'thumbnail': "https://lh3.googleusercontent.com/lo7CVdg8CpWyBmTC8yQFATLa1VeXGMUoULqwuk_jzNKJ1o9oTVzl4vFudiSz7vP9M5_DU0kvaWlNlz0=w120-h120-l90-rj"

    },
    {
        'title': 'Chamkila Remix - Vol Iv Nonstop',
        'artist': 'Amar Singh Chamkila',
        'musicUrl': 'https://music.youtube.com/watch?v=9BqsDzYYqQk',
        'thumbnail': "https://lh3.googleusercontent.com/rnt5et9hkwN_nCPtxDqPG8E8DPjepbh9yCOlzlXhOxQxuufg-UOz_SNF99vyunWMZrFvKZROm8BwmeA"
    },

    {
        'title': 'Sajjan Raazi',
        'artist': 'Satinder Sartaaj',
        'musicUrl': 'https://music.youtube.com/watch?v=t6vm8h5BDxo',
        'thumbnail': "https://lh3.googleusercontent.com/jM0rVpKP08tB9mOkgQjBrdFtxvsqVZaL7ta32jHqXUv8m1BqP0UVdjBW5ml12TF72-U89MCQdkavJMA"
    },

    {
        'title': 'Dil Cho Bhulana',
        'artist': 'Rana Ranjit',
        'musicUrl': 'https://music.youtube.com/watch?v=X7vUv03Kh8M',
        'thumbnail': "https://lh3.googleusercontent.com/O-j9leRtjHjiGBg7ofYgUmF4zRCXgnILn-SHsmbIjJCoF65xDzsE5zJTV5eLWzyclhx6XujiFb5iieue"
    },

    {
        'title': 'Wang Da Naap (feat. Sonam Bajwa)',
        'artist': 'Ammy Virk',
        'musicUrl': 'https://music.youtube.com/watch?v=bpXyk6sxsh4',
        'thumbnail': "https://lh3.googleusercontent.com/lYRZfLM2IkJjy0r1poLL7QLMHEzlXmdvoetonSZBoReHgOerrWV0SCIJqmSWHbbcG0PUoFyhUPm8hsHo"
    },

    {
        'title': 'Apsraa (feat. Asees Kaur)',
        'artist': 'Jaani',
        'musicUrl': 'https://music.youtube.com/watch?v=evxDX71hyhs',
        'thumbnail': "https://lh3.googleusercontent.com/N3rWV5jtvUMWyWja2FEP1fcVKZw6xUW_c0t33mBpGFs0VPDb0YBf7IHCv80JVrIZ5R3wj2JdKr5KFTKV"
    },

    {
        'title': 'Rangli Kothi',
        'artist': 'Amar Arshi',
        'musicUrl': 'https://music.youtube.com/watch?v=u_GYtaUskfI',
        'thumbnail': "https://lh3.googleusercontent.com/o8BtlN8tT4adXyAkS1eevLaTyI99u1Yk8Z8l9ny1HL9LANNkXmEpSCj89qCHQBGXH1RRpbyE4XT8EouynQ"
    },
    {
        'title': '8 Parche',
        'artist': 'Baani Sandhu',
        'musicUrl': 'https://music.youtube.com/watch?v=dZxW83XtbGg',
        'thumbnail': "https://lh3.googleusercontent.com/wQBIOIEQCx1l136Ex_zVwlfPy8qS4oOn9KY2nM3cQFdNvFAkBRtT9WaTSw_rk1dWrnlov5RX5i6WK0j-"
    },
    {
        'title': 'Libaas',
        'artist': 'Kaka',
        'musicUrl': 'https://music.youtube.com/watch?v=DUF46o6k7H8',
        'thumbnail': "https://lh3.googleusercontent.com/jmDQRcHexUk7gikfOVOtTFWnmrYMycVdIx1G9JigL2SXchEv_9viYlyuzsJdZYkC-62JVKI7ZzG3cEVA"
    },
    {
        'title': 'Patake (feat. Gurlez Akhtar)',
        'artist': 'Khan Bhaini',
        'musicUrl': 'https://music.youtube.com/watch?v=KdgtxCVDlVc',
        'thumbnail': "https://lh3.googleusercontent.com/Od7azoMIK9ze6S3x-gNwH2cHdPx1f3pd2jTRAu1qPd_4BmE9iW_FyDr9i-PclWG4HVHmks1nwyFJwNT0"
    },

    {
        'title': 'Dismiss 141',
        'artist': 'Korala Maan',
        'musicUrl': 'https://music.youtube.com/watch?v=vdXlh9IAeIM',
        'thumbnail': "https://lh3.googleusercontent.com/7nOg9wkuDJOGhBEnIZip7iaZwy0dsGmME3-wqsyNKm1ELJyKNzIRgbsGGiuxvA4tgD_hNqkhYHKMwjNg"
    },

    {
        'title': 'Feelinga',
        'artist': 'Garry Sandhu',
        'musicUrl': 'https://music.youtube.com/watch?v=3jPn54yv8Ao',
        'thumbnail': "https://lh3.googleusercontent.com/aq6wS5KaektsAYEI62OWwlYJCSdObeCyojK7Y8b4e2u9aKE1_qHWtTeR4LVs33NI-yo7a6-qWF6VXEd6eQ"
    },

    {
        'title': 'Diamond',
        'artist': 'Gurnam Bhullar',
        'musicUrl': 'https://music.youtube.com/watch?v=axLOunE36KY',
        'thumbnail': "https://lh3.googleusercontent.com/gKvpeAk4bXUAJj_TtJ8IGzacNn5BRgISDCnoDCZg6_Sz-hVJApE__WGgnPq0SCoo_nvNucZm0XlzoVI"
    },

    {
        'title': 'Hashar',
        'artist': 'Babbu Maan',
        'musicUrl': 'https://music.youtube.com/watch?v=AKLOY25uHeQ',
        'thumbnail': "https://lh3.googleusercontent.com/DMW9XpFOBYGAYwL3z1UbUaNCmUQmWnbvZGJJtf2-m2J4jPOky7_l0WwaYYqWPIk5ClpWNGCSQcbPUhg"
    },

    {
        'title': 'Rim Jhim (feat. Pav Dharia)',
        'artist': 'Khan Saab',
        'musicUrl': 'https://music.youtube.com/watch?v=xyAF7Mh95Ik',
        'thumbnail': "https://lh3.googleusercontent.com/D11cMia8iyo9bzH3ZtdnQFeK8YDfaZYi0IZ7p_PKsTIq0wCdZPvLl12B1dAU-bluzlYIppTSXwEKqxk"
    },

    {
        'title': '295',
        'artist': 'Sidhu Moose Wala',
        'musicUrl': 'https://music.youtube.com/watch?v=RTwknWM68oE',
        'thumbnail': "https://lh3.googleusercontent.com/rwoPrSpIkckdp1oDBOrKIlyd2tCWuGMHQmXDwusT68X6ZjApWOgSOeC5CGWRZWmDLBTdVi9PqBurHeIQ"
    },

    {
        'title': 'Motti Motti Akh',
        'artist': 'Shivjot',
        'musicUrl': 'https://music.youtube.com/watch?v=78jB6wmuzYI',
        'thumbnail': "https://lh3.googleusercontent.com/ITYRlI4KNIJchEgzGyMsecuAPbRyRKlmLaHQWtf0361jxKOGSXV4mjD092rr-uCyDGEy4hDva_Wr3Fva"
    },

    {
        'title': 'Big Men',
        'artist': 'R Nait',
        'musicUrl': 'https://music.youtube.com/watch?v=D9NegRRFQCg',
        'thumbnail': "https://lh3.googleusercontent.com/ETBL65tjb0l5-OJ9HgYfgJtXv7mRGbef_WXGyYfgpIbv8ydnJKwDcrpmnpO-QlYZUsBxvSw8AE-KIyrCNQ"
    },

    {
        'title': 'Aadat',
        'artist': 'Ninja',
        'musicUrl': 'https://music.youtube.com/watch?v=F5HhJGAP45Q',
        'thumbnail': "https://lh3.googleusercontent.com/cpybax4Y7vVBVGWbLko642YT2D6qDxt6lT5P9aX3dJh77datX8U3JDWpIR6ZiqQMtYqgwMKnv5a3_xnMAg"
    },

    {
        'title': 'Udaarian',
        'artist': 'Satinder Sartaaj',
        'musicUrl': 'https://music.youtube.com/watch?v=WqHzTIjoooQ',
        'thumbnail': "https://lh3.googleusercontent.com/ei_DHKmt4_iAuHKLJnUAxvYFjFMPX0dpLcILLsaE3lQJJdO6QELmv67aRPJh2mKv5XjbjkZ3qQaFMvCEgQ"
    },

    {
        'title': 'Sajjan Raazi',
        'artist': 'Satinder Sartaaj',
        'musicUrl': 'https://music.youtube.com/watch?v=t6vm8h5BDxo',
        'thumbnail': "https://lh3.googleusercontent.com/jM0rVpKP08tB9mOkgQjBrdFtxvsqVZaL7ta32jHqXUv8m1BqP0UVdjBW5ml12TF72-U89MCQdkavJMA"
    },

    {
        'title': 'Cheques',
        'artist': 'Shubh',
        'musicUrl': 'https://music.youtube.com/watch?v=OEo9mz8pljQ',
        'thumbnail': "https://lh3.googleusercontent.com/V_w7m2kuoVshpqcS1-RlEl-aONMQcGjP84WSo1tJS5IU8IDCr0v0s0NBMMGrLXtlL4CNjUKEdXcN3gAy"
    },

    {
        'title': 'Apsraa (feat. Asees Kaur)',
        'artist': 'Jaani',
        'musicUrl': 'https://music.youtube.com/watch?v=evxDX71hyhs',
        'thumbnail': "https://lh3.googleusercontent.com/N3rWV5jtvUMWyWja2FEP1fcVKZw6xUW_c0t33mBpGFs0VPDb0YBf7IHCv80JVrIZ5R3wj2JdKr5KFTKV"
    },

    {
        'title': 'Born to Shine',
        'artist': 'DILJIT DOSANJH',
        'musicUrl': 'https://music.youtube.com/watch?v=Lq0S1lqEjxo',
        'thumbnail': "https://lh3.googleusercontent.com/JZfP5dJhd0ZPZ_i1OPU0jtIVhMy0XD9r7bwBPMUkbZN4bafoTBYDO2t-Pyt6_wSf3a18ztwvOgYeSIM3"
    },

    {
        'title': 'Libaas',
        'artist': 'Kaka',
        'musicUrl': 'https://music.youtube.com/watch?v=DUF46o6k7H8',
        'thumbnail': "https://lh3.googleusercontent.com/jmDQRcHexUk7gikfOVOtTFWnmrYMycVdIx1G9JigL2SXchEv_9viYlyuzsJdZYkC-62JVKI7ZzG3cEVA"
    },

    {
        'title': 'Power Of Bhangra 31 Non-Stop Punjabi Remix(Remix By Dj Russie)',
        'artist': 'Romey Gill',
        'musicUrl': 'https://music.youtube.com/watch?v=PJbUJBHwJ5c',
        'thumbnail': "https://lh3.googleusercontent.com/VHxmjgxnNUORqZYAYwVdCs1g-I__6Y9DDUsECydFe18F5xj7k07kbQFBLNsh34WL_CobkSMvH6-7oPYSNw"
    },

    {
        'title': 'Tochan',
        'artist': 'Sidhu Moose Wala feat. Byg Byrd',
        'musicUrl': 'https://music.youtube.com/watch?v=ZXNZyVLCS_U',
        'thumbnail': "https://lh3.googleusercontent.com/vJSR8H3DJVEywF3a8HQIKtkhaeunT-awEcou9R7QzoseT5FLC_JoRxKjHH7mqh0aD690msgaTpBNyLw"
    },

    {
        'title': 'Aizak Ae Zaral',
        'artist': 'Ik Din Dulhan Hogi',
        'musicUrl': 'https://music.youtube.com/watch?v=GbgjZ0G6bkY',
        'thumbnail': "https://lh3.googleusercontent.com/NgXQlTgaR1dhVtruurv7xBfLJtuYQdQIW9Umnwo6EUNdz8U6l2U3f838poB8O6bVR_S03jGr0QngqjY8"
    },

    {
        'title': 'Elevated',
        'artist': 'Shubh',
        'musicUrl': 'https://music.youtube.com/watch?v=drEgWONDeBE',
        'thumbnail': "https://lh3.googleusercontent.com/uRTguCSN0CdMXt_KOPW1X5-aM1-VLpQrPamWLD6CnHhx0xAI0NgEzw_gFXdOXtSnx00AZwvPlNjpPFA"
    },

    {
        'title': 'Topper',
        'artist': 'Miss Pooja',
        'musicUrl': 'https://music.youtube.com/watch?v=xzAyZQmnHDQ',
        'thumbnail': "https://lh3.googleusercontent.com/dKkMFmsGuLmLmSdAzoShKvCHWWK-yNNQ2RhOUcLKog_l22XxoAsrSSzA0dRR_q-28Fxr9Rah8Mym-G8"
    },

    {
        'title': 'NARAZGI',
        'artist': 'NARAZGI',
        'musicUrl': 'https://music.youtube.com/watch?v=NLSII2-AXx4',
        'thumbnail': "https://lh3.googleusercontent.com/zku1IVsu760NUZZ6ZJL-MOTkUyF_6vtN_PPdiU7taYnsTkbMCxDMbI3V4Lk1fVusUb_OdbRghdhe68vv"
    },

    {
        'title': 'Hobbies',
        'artist': 'Singga',
        'musicUrl': 'https://music.youtube.com/watch?v=bsnCw8o4E5A',
        'thumbnail': "https://lh3.googleusercontent.com/PPHYvBtCtcOMVmAdEABFa_G94yiagp7VXmTBrx3wjX7A1YRFjyEMZ-9jAXbMwlbqAO1_AQoSjhMM9UUu"
    },

    {
        'title': 'Aashiq Purana (feat. Adaab Kharoud)',
        'artist': 'Kaka',
        'musicUrl': 'https://music.youtube.com/watch?v=vwvHtZYA8ho',
        'thumbnail': "https://lh3.googleusercontent.com/zFxm9HGAetP6nBQ73RO7rZi0c4R_N-wbB11YYPj0_htxiyDqPK1kxziVeI84rQ9wXMF9Yd1X3_66YL-M3g"
    },

    {
        'title': 'Sher-E-Panjab',
        'artist': 'Arjan Dhillon',
        'musicUrl': 'https://music.youtube.com/watch?v=OdQLAx6k7NY',
        'thumbnail': "https://lh3.googleusercontent.com/IoAG2kGPBYMVv4VDb3HPFZGO4OTULEyObVXn8QI59naPBf7XVGqDWTv7MvCeEr6UIkBJCyKWtDk0e_I2VQ"
    },

    {
        'title': 'Nakhre',
        'artist': 'Yaad',
        'musicUrl': 'https://music.youtube.com/watch?v=78RFNbJQ1XQ',
        'thumbnail': "https://lh3.googleusercontent.com/jt5h71RVyYsx-Pp9y4sQsFlVYSi-4gsfIMgeSzKuj5D5EmoL3DejHZ-x6AS4KjNQ-b16Kc1eP3icYtk"
    },

    {
        'title': 'Aaja We Mahiya',
        'artist': 'Imran Khan',
        'musicUrl': 'https://music.youtube.com/watch?v=qRTG8uF2ES4',
        'thumbnail': "https://lh3.googleusercontent.com/KwRJTlsKo9aMd2BxJuLn9zau3ogGOGA1828ZSPtXbAFB3PJ4DAo1SEVFEqvVRQrCfFcYlx4tgsqlAbgZ"
    },

    {
        'title': 'BATTUA',
        'artist': 'SURMA',
        'musicUrl': 'https://music.youtube.com/watch?v=b_KKY_0WLAI',
        'thumbnail': "https://lh3.googleusercontent.com/FaOGK6q673mqshUcrCNKhLNJj_NrY-DubacIkEb7hdMjlSpudrqGR6fYomVjdo-DiReuTXSwTGQ2VqM"
    },

    {
        'title': 'Asi Gabru Punjabi',
        'artist': 'Amrinder Gill',
        'musicUrl': 'https://music.youtube.com/watch?v=HtM_QDwghx8',
        'thumbnail': "https://lh3.googleusercontent.com/DQ8krwPY5R88VoyUaoyJHqjkUoG5Bh2K85NWnmzi9vdOM258i43D-bPnl-vn457EBcdWgcZdplpe5Nk"
    },

    {
        'title': 'Same Beef',
        'artist': 'Bohemia',
        'musicUrl': 'https://music.youtube.com/watch?v=34d2f8TYkaE',
        'thumbnail': "https://lh3.googleusercontent.com/CRQ8cRbaXAcm9GOj-wMavDdP-cilFvUHV9siyGmhNOwb4kzKCLj1cPSg24x8EqsKRP23XhObK-Re4tJmqA"
    },

    {
        'title': 'No Love',
        'artist': 'Shubh',
        'musicUrl': 'https://music.youtube.com/watch?v=jNkylY5HycI',
        'thumbnail': "https://lh3.googleusercontent.com/G2ryS0OQ-BJ4g94A315NXGxX3jGU0rph_zeqjBbKGkvMYQ56uLDsWHYZpLwmJmdUPZPxCE56Dw5w1fdjkA"
    },

    {
        'title': 'Amplifier',
        'artist': 'Imran Khan',
        'musicUrl': 'https://music.youtube.com/watch?v=xoWjZvAkD1M',
        'thumbnail': "https://lh3.googleusercontent.com/KwRJTlsKo9aMd2BxJuLn9zau3ogGOGA1828ZSPtXbAFB3PJ4DAo1SEVFEqvVRQrCfFcYlx4tgsqlAbgZ"
    },

    {
        'title': 'Greatest',
        'artist': 'Arjan Dhillon',
        'musicUrl': 'https://music.youtube.com/watch?v=ysEWMbGgrQ4',
        'thumbnail': "https://lh3.googleusercontent.com/5M_TL2TZwbSt2XZaEkO6Uj6gQ1Z9wJvN4mwGXYVWvog5I6HRxxCywrYX2IgWOxaOeb5ECZFRWvEw4S_j"
    },

    {
        'title': 'Top Notch Gabru',
        'artist': 'vicky',
        'musicUrl': 'https://music.youtube.com/watch?v=pPvtmBNHg0M',
        'thumbnail': "https://lh3.googleusercontent.com/Wh8xtJ2S7BofX1PGUONwM32DlrMWXg0eNfEFm2Wp6Ca3cUJ8cGMqPGeyzJRSggFgSmZQZNV4guCcEjRcbg"
    }


]


musicData2 = [
 
{'musicUrl': 'https://music.youtube.com/watch?v=l3g5c-yx2pU', 'title': 'Sade Jehe', 'artists': 'R Nait & Black Virus & Sade Jehe', 'thumbnail': "https://lh3.googleusercontent.com/P5dRP_E_Qy9J3ihsOv8v3GrHckwW1H4oKjTx6P0wlROYvNljFej2Iprqi85HimEuEHdFsXtXRxN1XYW_=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=oAqItl1De9s', 'title': 'Defaulter', 'artists': 'R. Nait & Gurlez Akhtar & Defaulter', 'thumbnail': "https://lh3.googleusercontent.com/y4TQGBLTCgb_Quu9i6lZTaL1HPKSiesvu_YTlGuo4oQJsEn9piqOWrTUu11AtNVgAN_oZpxBaoxOmTE=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=m-CkvFP9CFA', 'title': 'Dabda Kithe Aa (feat. Gurlez Akhtar)', 'artists': 'R Nait & Dabda Kithe Aa', 'thumbnail': "https://lh3.googleusercontent.com/70JG0HIKskT9GZYGixynvwm3iXQqcQA7Y6_4Q5nzfXWjAAmU_UCua4nR7eZ6Jvrm_vGBAtxN3KEORR-E=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=wZjUWMlv0sM', 'title': 'Majak Thodi Ae', 'artists': 'R Nait & Gurlez Akhtar & Majak Thodi Ae', 'thumbnail': "https://lh3.googleusercontent.com/nIrFAtGoBpCx5B6RVMFR7_9tnTy11OsArAZEQCBrywm2VbV8A6GWAwNoXjN0iygO30vUec6UhQkJMHk=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=PWtC0e44OuI', 'title': 'Reela Wala Deck (feat. Labh Heera)', 'artists': 'R Nait & Reela Wala Deck', 'thumbnail': "https://lh3.googleusercontent.com/kjSq9VVP3enimF_e0bFipVj6hPShT0aXhtdNlNoPxr7IDQVnKFmxCwpyL_P6sIQ8BA44sl3sY3cw_a_X=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=28A_PilA6Wk', 'title': 'Value', 'artists': 'R Nait & Gurlez Akhtar & Value', 'thumbnail': "https://lh3.googleusercontent.com/mwuNcbhLaO4bWfbC_sm3uIsykzHExeHJ0anWSeiP-91btoZFJMbJF6Giz1cZi2GKRwkMNKk0XEGxDy03=w120-h120-l90-rj"},
 
{'musicUrl': 'https://music.youtube.com/watch?v=WO-IxNytrKA', 'title': 'Kaali Range (feat. Gurlez Akhtar)', 'artists': 'R Nait & Kaali Range', 'thumbnail': "https://lh3.googleusercontent.com/ol1aMk1yR1n-LXVJXh_uoj6t4nAcQfrPSCE6vXIlLe7EcesNCqlgPJgt-ouY8S6PcQAiTMWIBUTVNGCQ=w120-h120-l90-rj"},
 
{'musicUrl': 'https://music.youtube.com/watch?v=u4Q7w2GhQUI', 'title': 'Future', 'artists': 'R Nait & Gurlez Akhtar & Future', 'thumbnail': "https://lh3.googleusercontent.com/6MSYr7NptwAO5tTtGugrv3NEHxOHbgYKeeiRp0nv6uEJYuYLuRRkxY4UaLYipLVBEE3sNt2_r6Vp3Qo=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=PAEu2_RJy5Y', 'title': 'U Turn (feat. Shipra Goyal)', 'artists': 'R Nait & U Turn', 'thumbnail': "https://lh3.googleusercontent.com/1uON1eR4a01bhw42QgtAFWEzK42xbP2utZFEG1QAwQCajw7ROyseoWMyTJAOhIi6fQE_KWvJ589aVZLF=w120-h120-l90-rj"},

 
{'musicUrl': 'https://music.youtube.com/watch?v=1ybuSWsEsdY', 'title': 'Shakeeni', 'artists': 'Gurnam Bhullar & Shakeeni', 'thumbnail': "https://lh3.googleusercontent.com/LP65EDTbppHvMIKKBhHVtApWzWCMT8GijoSZEcILhcduS1jG8oK-oxu-NsszHQpf4GeGTe7o9qPwdvzn=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=GwHjCzXX9mA', 'title': 'Pagal', 'artists': 'Gurnam Bhullar & Pagal', 'thumbnail':"https://lh3.googleusercontent.com/BgO0L9T-fV-V3qNPvuwGhEmxOpj3SYnqi5InQ4kO9bGl9TpdvwyrvgXE1W-8ihcQAgglkS6s5LwzBbl1=w120-h120-l90-rj" },

{'musicUrl': 'https://music.youtube.com/watch?v=fMA7VlDcUc4', 'title': 'Wakh Ho Jana', 'artists': 'Gurnam Bhullar & Main Viyah Nahi Karona Tere Naal (Original Motion Picture Soundtrack)', 'thumbnail': "https://lh3.googleusercontent.com/TBqSJOfAvZXcvuJBSw2PV4GopK_Ovn5_ECH4FJw8UJ8LWB6SRmZYK8CeeY2F6NUtcNjdSYXCxADWU7w=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=8PcqJRypiQk', 'title': 'Mera Yaar (From "Lekh")', 'artists': 'Gurnam Bhullar & B Praak & Mera Yaar (From "Lekh")', 'thumbnail': "https://lh3.googleusercontent.com/romud4pX8ySyYrqa3iTxQWXwx7dDEzS33RiHoEukW9IBH1XpByA8Ix0_ND9p-5wlOr2yI1vt713u9R_x=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=5iLqq0BP-vE', 'title': 'Waake', 'artists': 'Gurnam Bhullar & Waake', 'thumbnail': "https://lh3.googleusercontent.com/K4XPjtJ6EAh8ppIIjYqnb5p8PbuAu9KAt-RYNsz7AlDkhYtrO_nyoINy61TX6mhLB_Gph6jtS5y_V3cT=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=c_bYyPGXEOc', 'title': 'Pent Straight', 'artists': 'Gurnam Bhullar, Kaptaan & Desi Crew & Majestic Lane', 'thumbnail':"https://lh3.googleusercontent.com/iy6fG8FsFLwCAJnrDnISvpqT7udQ2MaDnWCA57pKO_WM_TAXcIbEwygX-xJ5NcPSiQRC3kE7gLWr9HU=w120-h120-l90-rj" },
 
{'musicUrl': 'https://music.youtube.com/watch?v=nzMIaolk3YQ', 'title': 'Jija Saali', 'artists': 'Gurnam Bhullar & Deepak Dhillon & Jija Saali', 'thumbnail': "https://lh3.googleusercontent.com/wRsjqwYoXPIsdChCnRt9g0VjDQ0tSW0S-Zg7qlU_hbG_pdi-vcfHRGQDk3ZGvWGtbMrbRlzRihlk0nao-Q=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=MbTkddFU74o', 'title': 'Phone Maar Di', 'artists': 'Gurnam Bhullar & Phone Maar Di', 'thumbnail': "https://lh3.googleusercontent.com/OIwlUKO9szzTx1yjwfKhZ5PlhiltPhvMxeca1Umdf1zz-SdREeyL4720d2h4Bp7rbk5BfwyZOZpEx8nv=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=AJz03Wrlaf0', 'title': 'Kabil', 'artists': 'Gurnam Bhullar & Kabil', 'thumbnail': "https://lh3.googleusercontent.com/Pr04_zyt6ArHdjG9vUMzif3v76YFuZMsuRAgO45q97fTjpDNeQoXMpM03ddsDINSbq_SFZ2Iy6SB5T4r=w120-h120-l90-rj"},


{'musicUrl': 'https://music.youtube.com/watch?v=pZbYSwCEdA0', 'title': 'Dollar (From "Dakuaan Da Munda")', 'artists': 'Sidhu Moosewala & Byg Byrd & Dollar (From "Dakuaan Da Munda")', 'thumbnail': "https://lh3.googleusercontent.com/Dy_IhF5lu0uR0DUWkaVW7SDWruRD8oUPrbkviBsOs56j-ONBnzk-EK_z4Q2Z3dah_6lkbJNmIcZMOtU=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=sKK6MOdXrG0', 'title': 'So High', 'artists': 'Sidhu Moose Wala & So High', 'thumbnail': "https://lh3.googleusercontent.com/lZjmzE_j1SYPAJH4yl2Vs3rm7y267os3_NiXQhb15grls1YvgxSlK99VGvY5zJhCKTrCemqM38gx3pAy1A=w120-h120-s-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=_dHmtIcvFag', 'title': 'East Side Flow', 'artists': 'Sidhu Moose Wala & East Side Flow', 'thumbnail': "https://lh3.googleusercontent.com/nXTSh0NNQLJtskj4dBnQjtKzzOjXrhkzL6OxBBHPKrhhLWkY4BQds_is1SZI1YMiIQKcNUWJK1qkwE28=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=Na_4wSZp3t4', 'title': 'GOAT', 'artists': 'Sidhu Moose Wala & Moosetape', 'thumbnail':"https://lh3.googleusercontent.com/rwoPrSpIkckdp1oDBOrKIlyd2tCWuGMHQmXDwusT68X6ZjApWOgSOeC5CGWRZWmDLBTdVi9PqBurHeIQ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=izq8HEaKt4I', 'title': 'Badfella', 'artists': 'Sidhu Moosewala & Pbx 1', 'thumbnail': "https://lh3.googleusercontent.com/RDWYxn9Rlgqe4LQ9x22zUg99Q67M5p1h1MQP4pUk5leRmrxFKSbaUQF9Yg8rSn0QVP2v0XhmhU97XqaZ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=YFFLEdEOpEM', 'title': 'Dawood', 'artists': 'Sidhu Moosewala & Pbx 1', 'thumbnail': "https://lh3.googleusercontent.com/RDWYxn9Rlgqe4LQ9x22zUg99Q67M5p1h1MQP4pUk5leRmrxFKSbaUQF9Yg8rSn0QVP2v0XhmhU97XqaZ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=T7dgB7MCfIk', 'title': 'Calaboose', 'artists': 'Sidhu Moose Wala & Moosetape', 'thumbnail': "https://lh3.googleusercontent.com/rwoPrSpIkckdp1oDBOrKIlyd2tCWuGMHQmXDwusT68X6ZjApWOgSOeC5CGWRZWmDLBTdVi9PqBurHeIQ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=XWg6c2keJCk', 'title': 'Levels (feat. Sunny Malton)', 'artists': 'Sidhu Moose Wala & Levels', 'thumbnail': "https://lh3.googleusercontent.com/2QyBELnDbh_coHWHn42JtAtukazpWfywm5eQJK6uvQIm2xsu70rmD20nyoTUr767N2P_hvEPdEw2FkhmfQ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=ZXNZyVLCS_U', 'title': 'Tochan', 'artists': 'Sidhu Moose Wala feat. Byg Byrd & Tochan', 'thumbnail': "https://lh3.googleusercontent.com/vJSR8H3DJVEywF3a8HQIKtkhaeunT-awEcou9R7QzoseT5FLC_JoRxKjHH7mqh0aD690msgaTpBNyLw=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=5nhq_scnUPE', 'title': 'Death Route', 'artists': 'Sidhu Moosewala & Pbx 1', 'thumbnail': "https://lh3.googleusercontent.com/RDWYxn9Rlgqe4LQ9x22zUg99Q67M5p1h1MQP4pUk5leRmrxFKSbaUQF9Yg8rSn0QVP2v0XhmhU97XqaZ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=3BB46cdoQKI', 'title': "I'm Better Now", 'artists': 'Sidhu Moosewala & Pbx 1', 'thumbnail': "https://lh3.googleusercontent.com/RDWYxn9Rlgqe4LQ9x22zUg99Q67M5p1h1MQP4pUk5leRmrxFKSbaUQF9Yg8rSn0QVP2v0XhmhU97XqaZ=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=ohWtIcNFw1Y', 'title': 'Malwa Block', 'artists': 'Sidhu Moose Wala & Moosetape', 'thumbnail': "https://lh3.googleusercontent.com/rwoPrSpIkckdp1oDBOrKIlyd2tCWuGMHQmXDwusT68X6ZjApWOgSOeC5CGWRZWmDLBTdVi9PqBurHeIQ=w120-h120-l90-rj"},

 
{'musicUrl': 'https://music.youtube.com/watch?v=qRBDz7tCCbk', 'title': 'We Rollin', 'artists': 'Shubh & We Rollin', 'thumbnail': "https://lh3.googleusercontent.com/Z52VtxBQZEZ80bb_gWFoun-50H9BC_hdRkExyQUzp3Rdx8OOoPiz1tJGzWF5WHwyyb0k7IOT7fLMI7uF=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=h4SGsHUr4SA', 'title': 'Baller', 'artists': 'Shubh & Ikky & Baller', 'thumbnail': "https://lh3.googleusercontent.com/TMs8F36tog6BNOxTQhxdfa_NwGlGSxctjDOk1GpFiblDD2GGeo-gwXbq5tqqohMSwAJawqI9p8fnI1E=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=1usErKKsNGM', 'title': 'King Shit', 'artists': 'Shubh & Leo', 'thumbnail': "https://lh3.googleusercontent.com/5sAOVCBCsvjDwhvdr_AakxsrmLi28MOqvkPI_K39v6jkHIGGI_3yZcAHlauA0PrPx5Te8uEX98zAnyPf=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=Zw9zc9otxek', 'title': 'Her', 'artists': 'Shubh & Her', 'thumbnail': "https://lh3.googleusercontent.com/3MOLy9UxekpRnVAddfnRM6jZiv5LXtTMDRLSvHSYecVPlAmWuV3Zixc2Zo7Q6Q2S4008KyPv6Lu-iBiVyg=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=_J1GeX1iRWg', 'title': 'Offshore', 'artists': 'Shubh & Offshore', 'thumbnail': "https://lh3.googleusercontent.com/DxR4v0BszYSxcnHZhXlEcVdSNDr3MYIuGupSpClZ2wTwnnhW6dCpyXjc9_9rupJC5ltZ6jxgECQ__a27=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=1FdMm_O7it8', 'title': 'One Love', 'artists': 'Shubh & One Love', 'thumbnail': "https://lh3.googleusercontent.com/1L5hDbqWRfzoPbCYQtNJLMqIr3KLQB4a0uzkkm8M_Ef9GrXsGkmdVp46dx6JDKr_h0qUPBlOJCYumds=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=5tzXovJu_HE', 'title': 'Shubhaarambh', 'artists': 'Amit Trivedi, Shruti Pathak & Divya Kumar & Chak De! Jeet Le!', 'thumbnail': "https://lh3.googleusercontent.com/qnzA4uVwPv9BtexFJrBxvoSs8FsI8dGPVXPpydTNvDyqZusWKf0KByIHgk2x-Hb2WBO4IBvcDctQ3IcL=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=x18b0D8sTwo', 'title': 'Excuses', 'artists': 'AP Dhillon, Gurinder Gill & Intense & Excuses', 'thumbnail': "https://lh3.googleusercontent.com/YodB8IMuc531lUrvJBl5gwh5yl242hTBKfVj-cpk4oFOqOm-wElw5Lcw3_DvagrR0arcXXs19l6xr6MN5Q=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=h_tAzU95CNE', 'title': 'Schedule', 'artists': 'Tegi Pannu & Mani Sidhu & Schedule', 'thumbnail': "https://lh3.googleusercontent.com/UsAdIwiVf5iESpPGeH95usgNKLeVskDPKL45AhB4GfaeMduEwi9DSRbSU6AC9v_0EvH0G7xmXx25Vgw=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=8DvIsGhtfY8', 'title': 'Bandana', 'artists': 'Shubh & Bandana', 'thumbnail': "https://lh3.googleusercontent.com/HXBedjoDxkPIOhwWIzUrEdQYwUyK9hpgCBhChwMRY-1E8Jver3T-NVKXutwWzAhNBDPXCdtqVogApWL8=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=Z92NElFi0k0', 'title': 'SUBAH SUBAH LE SHIV KA NAAM KAR LE BANDE YE SHUBH KAAM', 'artists': 'HARIHARAN, ARUN PAUDWAL and NANDLAL PATHAK & SHIV MAHIMA', 'thumbnail': "https://lh3.googleusercontent.com/owTzg7u2xGQIInzdJkvdW4i0FznVwNpfH91affB4HEkNlRxkV1Ts0VfSG_zfZXv_PJvfHpF4aVNXcJQZ-w=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=vsrjh8ip9-0', 'title': 'You and Me', 'artists': 'Shubh & Leo', 'thumbnail': "https://lh3.googleusercontent.com/5sAOVCBCsvjDwhvdr_AakxsrmLi28MOqvkPI_K39v6jkHIGGI_3yZcAHlauA0PrPx5Te8uEX98zAnyPf=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=wLRDsTCphbw', 'title': 'Still Rollin', 'artists': 'Shubh & Still Rollin', 'thumbnail': "https://lh3.googleusercontent.com/V_w7m2kuoVshpqcS1-RlEl-aONMQcGjP84WSo1tJS5IU8IDCr0v0s0NBMMGrLXtlL4CNjUKEdXcN3gAy=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=FM2ykrYbzqg', 'title': 'Brown Munde', 'artists': 'AP Dhillon, Gurinder Gill & Shinda Kahlon & Brown Munde', 'thumbnail': "https://lh3.googleusercontent.com/YTBCHTjI5MrB9HFTDisDJmjMFdKyrq0ZNahCImeA-lkwARod4UdgdfH95z3bhJa6ObMIvz1Nksm_Dy4=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=9SoY4BtR8Pw', 'title': 'Safety Off', 'artists': 'Shubh & Leo', 'thumbnail': "https://lh3.googleusercontent.com/5sAOVCBCsvjDwhvdr_AakxsrmLi28MOqvkPI_K39v6jkHIGGI_3yZcAHlauA0PrPx5Te8uEX98zAnyPf=w120-h120-l90-rj"},


{'musicUrl': 'https://music.youtube.com/watch?v=Nl4ydD4Bhk4', 'title': 'Temporary Pyar (feat. Adab Kharaud)', 'artists': 'Kaka & Temporary Pyar', 'thumbnail': "https://lh3.googleusercontent.com/ZEouPCxi6kv3BQGjEQ9dk9uOu8xXP6_bdJ-NvQH1wIoQNnSxzrvkjm7NME1-NjtIi3KqX1Ld8ShTAQM=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=3hiOTdUu520', 'title': 'Mitti De Tibbe', 'artists': 'Kaka & Mitti De Tibbe', 'thumbnail': "https://lh3.googleusercontent.com/aEMVx7DA7l_o29CAq06aOcVPxQayP0CU2NACxMey8AKohD-H0lbPGp2I_ECgk9P9Cadcn1_zMNAkJb08=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=vwvHtZYA8ho', 'title': 'Aashiq Purana (feat. Adaab Kharoud)', 'artists': 'Kaka & Aashiq Purana', 'thumbnail': "https://lh3.googleusercontent.com/zFxm9HGAetP6nBQ73RO7rZi0c4R_N-wbB11YYPj0_htxiyDqPK1kxziVeI84rQ9wXMF9Yd1X3_66YL-M3g=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=ty52ErnbOh4', 'title': 'Mere Warga', 'artists': 'Kaka & Mere Warga', 'thumbnail': "https://lh3.googleusercontent.com/YzsDSJ7suBWe99lGBOWQBourQrRusDnspBAQgYgCmOyTGTl0eglJZqL-kp1hLqs-bBvy_cpQbFLzdB4Y=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=JBB3X25QK0I', 'title': 'Didaar', 'artists': 'Kaka & Didaar', 'thumbnail': "https://lh3.googleusercontent.com/vuItL-sZKNnbX69EpZD4LQykSK8ALshGDK2O5FQSUyaG_HVUsYqtAJ57iZbthL09APXNS1nSRuE5oRo=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=-ATV3mIvbHg', 'title': 'Ki Likha', 'artists': 'Kaka & Ki Likha', 'thumbnail': "https://lh3.googleusercontent.com/Fl4msRaSn2V5D_3fvyeYiMlpPhhLd53GjQ1uwOIMJp8v7ez4Nv3SJz6i23-3vCvPVGYtrfwu7XbszUUP=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=5uzLmkgLiwM', 'title': 'Keh Len De (feat. Inder Chahal & Himanshi Khurana)', 'artists': 'Kaka & Keh Len De', 'thumbnail': "https://lh3.googleusercontent.com/pDIEeqmj6LqHGUiRkOs62kSI1HkqNgM9ShfE5haIWCG1sXdan3fvapoDzjIgh7deltLZcLsTAJbuN9UD=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=of2_E7Ab16s', 'title': 'Dhoor Pendi (feat. Karan Ambarsariya)', 'artists': 'Kaka & Dhoor Pendi', 'thumbnail': "https://lh3.googleusercontent.com/f6Kop58s9Wi31ei5ZnQDpWEpTkDLZZlmAf7v8xMpoCjpfQxjfK58DCTetL2p_sRygtlzOnxndYkqfJqF=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=ZWTauP2vQKw', 'title': 'Bholenath (A Love Story)', 'artists': 'Kaka & Bholenath (A Love Story)', 'thumbnail': "https://lh3.googleusercontent.com/qWoWop4wJx_Lr9mlY0S6KiBK2b2-iyysRtqX-4ukD9EQnLohX-mjbHMpxUgbpKA5Ca8o6x6CyuvD8jpu=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=nHsfQVpp7DI', 'title': 'Nishaan (feat. Deep Prince)', 'artists': 'Kaka & Nishaan', 'thumbnail': "https://lh3.googleusercontent.com/d_IEECO2zbx42Xs5Vc9rtFbz7PuWRFDjDZWtxxzot81G1IsltMSK_USwhccH19RlX7Y-6kM95YN31jw=w120-h120-l90-rj"},


{'musicUrl': 'https://music.youtube.com/watch?v=WBbv3gc0ZKc', 'title': 'Difference', 'artists': 'Song & Amrit Maan & Difference', 'thumbnail': "https://lh3.googleusercontent.com/SWfc_VXE5fLDS8ObTLmQVmxE8TFvBP5XM07D24JSGcFxe6j1obAiQc2vaQdY54Acr1gSHVSJznTa30keww=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=4FP5jbnKm2s', 'title': 'Combination', 'artists': 'Song & Amrit Maan & Combination', 'thumbnail': "https://lh3.googleusercontent.com/mZijLM-3I0e08umlVmFwyjtH2KHvZRTaC0Zm5FlDrhKHJKXyNZzt6ba404gBI_OqhhK1SsTbOaq-Lzvv=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=4gxn3mOQl08', 'title': 'Bambiha Bole', 'artists': 'Amrit Maan & Sidhu Moose Wala & Bambiha Bole', 'thumbnail': "https://lh3.googleusercontent.com/1kBitW2r3l4g2lK1Ij9hJ43WdBskhrZXrFfQ8mToaknSKqcdhqg_m1mn1Z6whqaNfIB3YikSuUvdVd8mKA=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=GyM7svPvejo', 'title': 'The King', 'artists': 'Amrit Maan & The King', 'thumbnail': "https://lh3.googleusercontent.com/-xLjrgfz94Urs8I86Bh2Ly-gx0X3-dFnCwmLP5VI76x3eZmMGXUR56UZkxpjfUo7AWApZU-8aZkase-t=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=_R1CBoKfvbk', 'title': 'Mithi Mithi', 'artists': 'Amrit Maan & Mithi Mithi', 'thumbnail': "https://lh3.googleusercontent.com/D2cXNkTvXOcDKQ9Q-Kup1UsW3g5ZWVFKFzNhzOL1180_6Bo0SDJWdI8yhOveZLz52n3ZZLAWxxX31mgm=w120-h120-l90-rj"},

{'musicUrl': 'https://music.youtube.com/watch?v=eyaBZNrntxs', 'title': 'Allah Maaf Kre (feat. Tehzeeb Hafi)', 'artists': 'Video & Amrit Maan & 19M views', 'thumbnail': "https://i.ytimg.com/vi/eyaBZNrntxs/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3lR7zKMA8s4g81VVMGM2EmZa6t_Dg"},

]
download_folder = 'C://Users//visha//Desktop//Music_player//Home//music//static//music//artists//newartist'

# os.makedirs(download_folder, exist_ok=True)

# for song in musicData2:
#     try:
#         video_id = song['musicUrl'].split('v=')[1].split('&')[0]
#         video_url = f'https://www.youtube.com/watch?v={video_id}'

#         output_template = os.path.join(download_folder, f"{song['title']}.mp3")

#         with yt_dlp.YoutubeDL({
#             'outtmpl': output_template,
#             'format': 'bestaudio/best',
#             'noplaylist': True,  
#         }) as ydl:
#             ydl.download([video_url])

#         print(f"Downloaded: {song['title']} by {song['artist']}")

#     except Exception as e:
#         print(f"Error downloading {song['title']}: {str(e)}")

import requests
from PIL import Image
from io import BytesIO
import os
# def download_image(image_url, title, folder):
#     try:
  
#         os.makedirs(folder, exist_ok=True)

    
#         response = requests.get(image_url)
#         response.raise_for_status()  

       
#         img = Image.open(BytesIO(response.content))

       
#         file_path = os.path.join(folder, f"{title}.jpg")

      
#         img.save(file_path)
#         print(f"Image '{file_path}' saved successfully!")
#     except Exception as e:
#         print(f"Error downloading {title}: {e}")

# for data in musicData2:
#     download_image(data['thumbnail'], data['title'], download_folder)


def save_artists_to_txt(artists, folder, title):
    try:
        # Ensure the folder exists
        os.makedirs(folder, exist_ok=True)

        # Construct the full path to save the artist names as a text file
        text_file_path = os.path.join(folder, f"{title}.txt")

        # Write the artist names to the text file
        with open(text_file_path, 'w') as file:
            file.write(artists)
        print(f"Artists '{artists}' saved in '{text_file_path}' successfully!")

    except Exception as e:
        print(f"Error saving artists for '{title}': {e}")

# Save artist names for each song into individual text files
for data in musicData2:
    save_artists_to_txt(data['artists'], download_folder, data['title'])