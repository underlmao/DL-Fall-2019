import numpy as np
import io
import matplotlib.colors
import matplotlib.pyplot as plt


RNN1024_100 = [
[2.186671247187349, 1.6300752945957548, 1.4929343586642192, 1.4331455787256997, 1.3984350975553488, 1.3742536397675527, 1.3557478779370022, 1.3478286117095835, 1.3334846666881017, 1.3223116896465004, 1.3145219438732636, 1.3105190909839344, 1.3027720098467392, 1.2976770832893247, 1.2931122456804818, 1.3013750592106748, 1.2916735819759004, 1.292725907158606, 1.2867175770789077, 1.2857566682158232, 1.2962944256539548, 1.2873538736040007, 1.2860083004160727, 1.293689133843547, 1.2895788777734816, 1.3048544992227793, 1.2828508626027733, 1.2929468393676937, 1.2875582761020126, 1.3191007491590698]
,[1.824784150965074, 1.6455188885857073, 1.5815417704862702, 1.549835416008444, 1.5306952846751491, 1.5050851844338813, 1.4968260821174173, 1.4948876594094664, 1.4905713743322035, 1.4864484629911534, 1.4856697576186235, 1.4928013880112592, 1.4797386932373047, 1.483499594295726, 1.4769006347656255, 1.4863864808924057, 1.4805242022346046, 1.4847546296961165, 1.4776942533605235, 1.4824627506031707, 1.4801350402832032, 1.4820130202349495, 1.4803481741512519, 1.4835889793844788, 1.4864577125100524, 1.4896191540886374, 1.4863485179227944, 1.4956717861399926, 1.4894711932014015, 1.5119766998291015]
,[38.47, 51.19, 54.75, 56.24, 57.12, 57.72, 58.21, 58.41, 58.81, 59.09, 59.32, 59.44, 59.66, 59.8, 59.93, 59.67, 59.91, 59.88, 60.05, 60.08, 59.79, 60.01, 60.05, 59.86, 59.97, 59.5, 60.12, 59.89, 60.01, 59.19]
,[46.36, 51.18, 52.67, 53.67, 54.24, 54.98, 55.53, 55.47, 55.52, 55.71, 55.75, 55.47, 55.79, 55.86, 55.81, 55.75, 55.83, 55.78, 56.08, 55.56, 56.09, 55.88, 55.75, 55.66, 55.9, 55.54, 55.78, 55.56, 55.76, 54.84]
]
GRU1024_100 =[
[1.9787741311344378, 1.4596223769728671, 1.3648530192157482, 1.3195988675455983, 1.2900221742832256, 1.2668989959978039, 1.2482465275608563, 1.2326468650652136, 1.2186432332458834, 1.2061939355375488, 1.1953501339689094, 1.1854778487833328, 1.1773388366460449, 1.1696673816012353, 1.1642105375719702, 1.157949027853616, 1.15434009477562, 1.1509459355793927, 1.148323654952913, 1.1468717242551307, 1.1460575393794739, 1.1464470038533385, 1.1468221733952833, 1.1474919262971723, 1.1495093337214923, 1.1515799320147913, 1.155427025589922, 1.1580615549270112, 1.1625202827495749, 1.1674775069521874]
,[1.6522121833352486, 1.5246156759823069, 1.486060449936811, 1.4573462991153492, 1.4489165586583757, 1.442120056152344, 1.4371492767333984, 1.4339117072610295, 1.440684976016774, 1.43547929202809, 1.440878834443934, 1.4459874725341797, 1.4488361089369828, 1.450776874317842, 1.4553372327019183, 1.461936232622932, 1.4618164645924285, 1.4682087348489201, 1.4677403573428884, 1.4730545088824105, 1.4756752328311695, 1.4765031657499423, 1.4743041633157175, 1.4823882024428425, 1.4877997723747702, 1.4816542053222654, 1.4824624768425434, 1.4872701936609605, 1.484722788193647, 1.4857694782930257]
,[43.16, 55.72, 58.12, 59.26, 60.03, 60.67, 61.22, 61.68, 62.11, 62.5, 62.85, 63.16, 63.44, 63.72, 63.92, 64.13, 64.26, 64.39, 64.51, 64.55, 64.58, 64.6, 64.6, 64.59, 64.51, 64.46, 64.33, 64.24, 64.11, 63.95]
,[50.99, 54.42, 55.6, 56.22, 56.55, 56.66, 56.73, 57.09, 56.97, 57.15, 56.99, 56.91, 56.91, 56.83, 57.0, 56.71, 56.77, 56.51, 56.64, 56.62, 56.7, 56.57, 56.67, 56.44, 56.62, 56.57, 56.69, 56.41, 56.43, 56.39]
]
LSTM1024_100 = [
[1.9805043814635241, 1.4590814856260972, 1.3533303655124378, 1.302598393718343, 1.2677928283042514, 1.2406988944501693, 1.2174101846734273, 1.1962514852388968, 1.1771958225430024, 1.1585915826030613, 1.1411024042362667, 1.1251772607022428, 1.107899717448913, 1.0956933450979758, 1.079135620541355, 1.0672674338842176, 1.0538741064879258, 1.042552118097735, 1.0327734621529727, 1.0230521538647355, 1.0155853923185234, 1.009720284563101, 1.001904508677779, 0.996840175104071, 0.9920948177619957, 0.9877645744666436, 0.9837193399536065, 0.9822934292728666, 0.9806190643991742, 0.9779175771002566]
,[1.6504340093276078, 1.4974421198227823, 1.4557784181482651, 1.4291102734734027, 1.4144618000703701, 1.4069265343161186, 1.4042164724013388, 1.4011192793004654, 1.3986951536290788, 1.4018114875344674, 1.4151358884923597, 1.4145180780747353, 1.422317280488856, 1.4326888993207145, 1.4404082309498512, 1.4479829182344321, 1.4596972701128788, 1.4730742690142462, 1.4855682552562037, 1.4873072052001957, 1.4976370239257812, 1.5029415489645563, 1.5156244524787452, 1.521450276094325, 1.524255151187672, 1.5400707873176123, 1.532155272539924, 1.5423428120332607, 1.5436086452708526, 1.5505674115349262]
,[42.5, 55.66, 58.33, 59.62, 60.59, 61.32, 61.98, 62.63, 63.23, 63.83, 64.41, 64.93, 65.51, 65.97, 66.55, 66.98, 67.48, 67.91, 68.29, 68.63, 68.93, 69.17, 69.45, 69.67, 69.85, 70.03, 70.16, 70.21, 70.28, 70.36]
,[50.98, 54.89, 56.01, 56.73, 57.3, 57.66, 57.59, 57.89, 57.86, 57.83, 57.86, 57.81, 57.74, 57.52, 57.43, 57.3, 57.15, 57.05, 56.95, 56.95, 56.73, 56.75, 56.57, 56.4, 56.54, 56.25, 56.56, 56.35, 56.4, 56.12]
]
RNN512_100 = [
[2.187024864602686, 1.7167000547600073, 1.576137251460675, 1.506825850357539, 1.4658303640025705, 1.4381158021834182, 1.4191239647380733, 1.4038377931788673, 1.3921445172735447, 1.3818593680068565, 1.373635119998578, 1.366687638419015, 1.3602246421777446, 1.3551734396213986, 1.3503668764729564, 1.3468491197159083, 1.3427677979701047, 1.339469572405752, 1.3368686161968248, 1.3340614984944923, 1.3314592694323264, 1.3301709388246943, 1.3273585799516388, 1.3257419954167902, 1.3244306166849713, 1.3227039222689194, 1.3204008985162659, 1.3190435927816624, 1.3182315152242714, 1.3165685451083402]
,[1.8956715617460365, 1.7091579392377068, 1.6368265353932099, 1.5969120205149931, 1.5794214944278493, 1.5559540064194621, 1.5495748946245973, 1.541152128331802, 1.529762227675494, 1.5261456029555374, 1.525449075137868, 1.5173454553940715, 1.5142986566880172, 1.5120208156810087, 1.514546558155733, 1.5082150358312272, 1.5091431830911075, 1.5025815851548137, 1.503572683895336, 1.5050033569335939, 1.5053195728975182, 1.503660076365751, 1.4989140364703015, 1.5026871535357302, 1.4990184828814337, 1.5000055380428534, 1.502017458747415, 1.4975159319709328, 1.500544011733111, 1.501520192763385]
,[37.65, 48.62, 52.39, 54.21, 55.25, 55.97, 56.44, 56.82, 57.11, 57.34, 57.56, 57.72, 57.89, 58.03, 58.14, 58.24, 58.35, 58.43, 58.49, 58.58, 58.63, 58.67, 58.75, 58.79, 58.82, 58.89, 58.95, 58.99, 59.01, 59.05]
,[44.39, 49.58, 51.4, 52.48, 52.87, 53.82, 53.6, 53.84, 54.23, 54.46, 54.34, 54.47, 54.79, 54.89, 54.67, 55.08, 54.79, 55.18, 55.23, 55.16, 55.2, 55.19, 55.28, 55.09, 55.39, 55.36, 55.19, 55.29, 55.55, 55.3]
]
GRU512_100 =[
[2.0821518129031333, 1.547975397777136, 1.4333545822809302, 1.3826643957129634, 1.3518418472188913, 1.3309539277353413, 1.3154071755542671, 1.3022858353883071, 1.2915646020372415, 1.2826681567221572, 1.2745917041803847, 1.2674757149152798, 1.261087993283335, 1.256052344115739, 1.2501958110019982, 1.2459980503975554, 1.2420287750255377, 1.237837630800014, 1.2345257997512817, 1.2312636758161049, 1.2280179736189358, 1.2258451799580907, 1.2228887400676294, 1.2206406235168188, 1.2183693294497056, 1.216353006847477, 1.2145071853067457, 1.2131519247400568, 1.2115164540477634, 1.2101753047709964]
,[1.7270034969554227, 1.5763589477539062, 1.5208056281594668, 1.49479336458094, 1.4792764416862938, 1.469995821784524, 1.467372746187098, 1.4594441357780907, 1.4554292342242074, 1.4514919460521023, 1.453128913430607, 1.4532579489315258, 1.4541529307645908, 1.4532140664493336, 1.4543868031221274, 1.4535794740564683, 1.4511737958122701, 1.4553037441478054, 1.4553350874956923, 1.4569358421774474, 1.4527892213709215, 1.4543000972972195, 1.4554858039407172, 1.4543604502958407, 1.4620041162827437, 1.4612623147403494, 1.4623906348733342, 1.4609244941262638, 1.467077340518727, 1.4590167281206916]
,[40.05, 53.23, 56.19, 57.48, 58.24, 58.78, 59.2, 59.53, 59.81, 60.07, 60.27, 60.46, 60.64, 60.79, 60.96, 61.07, 61.2, 61.33, 61.42, 61.54, 61.62, 61.71, 61.79, 61.87, 61.94, 62.0, 62.06, 62.11, 62.16, 62.2]
,[48.98, 53.13, 54.54, 55.34, 55.8, 55.87, 56.14, 56.16, 56.58, 56.55, 56.62, 56.7, 56.59, 56.76, 56.69, 57.04, 56.97, 56.77, 56.73, 56.83, 56.83, 56.77, 56.84, 56.87, 56.77, 56.77, 56.82, 56.82, 56.61, 56.85]
]
LSTM512_100 = [
[2.0420957765101684, 1.560909706994957, 1.4422143369430296, 1.38668001681259, 1.3531785230748958, 1.3289409224520023, 1.311116050550267, 1.296426374185419, 1.2839410605240993, 1.2734748804516574, 1.2640340765375804, 1.2556143844601684, 1.2480801547574365, 1.24106437064411, 1.2347344670976912, 1.2288403997365083, 1.2229491122867995, 1.2177255360823844, 1.2130647263927208, 1.208457667978593, 1.2038229614364557, 1.2002329713992763, 1.195959800121886, 1.1920868628857237, 1.188264333622445, 1.184886078069066, 1.1821285184247856, 1.1787882641243128, 1.1753229382111854, 1.1728717424030333]
,[1.7383430705350984, 1.5874036093319164, 1.5270375016156361, 1.4951287033978629, 1.4753879906149472, 1.4620358770033892, 1.455603736428653, 1.444920717127183, 1.436449966430664, 1.4368990909352022, 1.434631975959329, 1.4328758329503675, 1.4303191555247585, 1.4289559487735524, 1.4259085711310893, 1.4274447227926814, 1.4225040211397058, 1.4241147119858684, 1.4253052655388325, 1.42718116311466, 1.4234359696332144, 1.4261176030776082, 1.4256481350169463, 1.4290652645335478, 1.4323675941018497, 1.427856117697323, 1.4355011210722077, 1.4356437638226676, 1.4352093416101788, 1.4385041764203237]
,[40.77, 52.87, 55.96, 57.35, 58.2, 58.79, 59.26, 59.62, 59.97, 60.25, 60.48, 60.72, 60.94, 61.12, 61.29, 61.45, 61.64, 61.8, 61.93, 62.07, 62.2, 62.34, 62.44, 62.58, 62.7, 62.79, 62.89, 63.0, 63.11, 63.19]
,[48.83, 52.8, 54.51, 55.31, 55.92, 56.07, 56.29, 56.67, 56.58, 56.81, 56.87, 57.2, 57.04, 57.19, 57.29, 57.26, 57.34, 57.3, 57.29, 57.19, 57.55, 57.32, 57.5, 57.21, 57.42, 57.32, 57.22, 57.26, 57.31, 57.29]
]
RNN1024_50 =[
[1.9090667682329112, 1.5292439843206567, 1.459493241211875, 1.4277867776142315, 1.4089948692420022, 1.3959473119753962, 1.3870084434857344, 1.38020189480364, 1.3747254528483543, 1.3708574519252146, 1.3684465390430645, 1.3662766168185942, 1.3646952075235452, 1.3633458558209597, 1.3625290181550846, 1.362252208570771, 1.3635712812015288, 1.363100912397271, 1.3638814832464223, 1.364160863681257, 1.3663228314268492, 1.3692261202533602, 1.3691605131269993, 1.3705817384698795, 1.3735871268511695, 1.3759266063516151, 1.379335200549751, 1.3790558025712385, 1.3837682525404593, 1.3868740561080382]
,[1.693472462529722, 1.6015394901883773, 1.5674032437974135, 1.557374933215155, 1.5496515843488166, 1.5423861561650818, 1.5367095504981882, 1.54023905215056, 1.529882976144985, 1.530466255519701, 1.529017539646315, 1.5278358813299648, 1.5323351453698204, 1.5340832674330556, 1.5299745333021968, 1.5302595166192534, 1.5402898550724642, 1.539037617116735, 1.5309795036868772, 1.537156511389691, 1.5360901652902794, 1.5368904025312784, 1.5440993599269703, 1.5426188770238898, 1.5390699613267098, 1.5474321514627207, 1.550318455350572, 1.5496750895182296, 1.5501820152393284, 1.5564440121858023]
,[43.88, 53.1, 54.81, 55.6, 56.04, 56.37, 56.6, 56.75, 56.89, 56.97, 57.03, 57.08, 57.15, 57.18, 57.19, 57.17, 57.16, 57.16, 57.15, 57.13, 57.08, 57.0, 57.01, 56.94, 56.87, 56.8, 56.69, 56.69, 56.57, 56.49]
,[48.76, 50.73, 51.79, 52.36, 52.57, 53.1, 52.92, 52.98, 53.14, 53.2, 53.0, 53.46, 53.08, 53.35, 53.47, 53.16, 53.01, 53.02, 53.22, 53.08, 53.26, 53.11, 52.93, 53.1, 53.0, 52.94, 52.67, 52.68, 52.81, 52.54]
]
GRU1024_50 =[
[1.781731048956612, 1.4281025395137235, 1.3695455323781398, 1.3397064736171889, 1.319834922147727, 1.3050148069551537, 1.2941753881832008, 1.2860228260972204, 1.279634821932486, 1.2752345263563245, 1.2721781543811688, 1.2701940775970224, 1.2690554967779197, 1.2697551793434587, 1.2706300527230179, 1.2726657011651046, 1.2758768638150493, 1.279703478062302, 1.2839753326903027, 1.2897797821197903, 1.29607625311135, 1.3027662723006528, 1.3104321898740385, 1.320294962462649, 1.332261576294636, 1.3453555461498987, 1.3692280968118011, 1.3895744141451658, 1.4245298339480246, 1.5187933975673056]
,[1.597632848767267, 1.52596580615942, 1.507075896332229, 1.4947009852312616, 1.4890515092490377, 1.4847696851647418, 1.4859405827176746, 1.4853021085435067, 1.4853389330877775, 1.4794500489165814, 1.4854772661734315, 1.4851961683190387, 1.4848747408217275, 1.4839970619091087, 1.4885446764075236, 1.4936721470045005, 1.4938569530542347, 1.4914245141070819, 1.4917437876825757, 1.5034006511301239, 1.5005346878715182, 1.5092904928456181, 1.5106789165994394, 1.5183945542487538, 1.5235751961970672, 1.5389513010218525, 1.5446673982039743, 1.5662038830743326, 1.6210260208793312, 1.8878917130180026]
,[47.12, 55.75, 57.24, 58.02, 58.58, 58.97, 59.3, 59.53, 59.75, 59.91, 60.0, 60.06, 60.1, 60.09, 60.08, 60.01, 59.93, 59.81, 59.69, 59.52, 59.32, 59.12, 58.9, 58.59, 58.26, 57.85, 57.14, 56.56, 55.56, 52.91]
,[51.13, 53.02, 53.52, 53.94, 54.23, 54.34, 54.56, 54.52, 54.61, 54.67, 54.47, 54.44, 54.51, 54.66, 54.53, 54.48, 54.3, 54.41, 54.53, 54.14, 54.24, 54.05, 53.95, 53.67, 53.46, 53.13, 52.98, 52.34, 50.83, 43.93]
]
LSTM1024_50 =[
[1.7882877135645212, 1.4198725454240622, 1.3525499472116354, 1.3158412455986142, 1.2890901784847728, 1.2677566077096925, 1.2490289557760827, 1.2327373540954085, 1.21770663249133, 1.2046160976004303, 1.1931490249016252, 1.1823646363482219, 1.1725864336716945, 1.1646176720472536, 1.1573591462121982, 1.151524048679624, 1.1458558706433744, 1.1412861473512965, 1.1383153208044192, 1.135193916872374, 1.133230111281428, 1.1322581688212154, 1.131133584435851, 1.131032471011192, 1.1315407766148482, 1.13242336965116, 1.1332790289318149, 1.1350714928793328, 1.1363367307177354, 1.1389289037369033]
,[1.586345626167629, 1.5053650344627485, 1.4773469587685397, 1.4648043889584752, 1.4577941164763075, 1.45314975462098, 1.4525296706047615, 1.4503801008583848, 1.4500868733723962, 1.4652866286125736, 1.4624688720703127, 1.4697618368397587, 1.4773393205283347, 1.473499837681867, 1.4883757726696953, 1.4935263127866003, 1.5052450362495757, 1.5011696790612268, 1.5066070092242694, 1.5096005558622054, 1.5187498827948087, 1.5136445772475091, 1.5113759181810467, 1.5165191937875062, 1.5253079489003052, 1.5178436323525253, 1.517154235839843, 1.5248166711779603, 1.5321038199162136, 1.5330034405252202]
,[46.49, 55.78, 57.46, 58.44, 59.15, 59.78, 60.31, 60.81, 61.29, 61.75, 62.12, 62.5, 62.82, 63.12, 63.38, 63.61, 63.79, 63.95, 64.06, 64.17, 64.25, 64.3, 64.33, 64.3, 64.3, 64.25, 64.23, 64.14, 64.07, 63.98]
,[51.22, 53.35, 54.33, 54.74, 55.21, 55.22, 55.23, 55.31, 55.22, 55.21, 55.18, 55.13, 55.01, 55.16, 54.76, 54.9, 54.8, 54.61, 54.65, 54.5, 54.53, 54.58, 54.52, 54.51, 54.38, 54.65, 54.55, 54.52, 54.39, 54.33]
]
LSTM2048_100 =[
[2.07666628929582, 1.4553477549939162, 1.3338076931387406, 1.272671513072872, 1.2282118902641825, 1.1874002269160588, 1.1454749216211737, 1.1003267650927289, 1.0504210676465715, 0.9984987345640719, 0.9475348750691702, 0.8977600084137671, 0.8552717529621321, 0.8206915603470557, 0.7891983898117897, 0.7648222921347583, 0.7440267352713752, 0.7289191962868545, 0.717891948827061, 0.7124612158457906, 0.7042228084425161, 0.7011631300593335, 0.6991258062564923, 0.6966772329649272, 0.6996202006255755, 0.7041295964342154, 0.7042807120286664, 0.7115271795480698, 0.7160497968783259, 0.7224799915160627]
,[1.682069567512064, 1.5119482421875, 1.4535552080939795, 1.4246940388399016, 1.4108050806382122, 1.4086112482407513, 1.4231207454905788, 1.4452445894129136, 1.4661611624325024, 1.5111191603716685, 1.5533793056712428, 1.5971075484331916, 1.6393080991857194, 1.6832509343764361, 1.7272305926154647, 1.75772242826574, 1.780920867919922, 1.8023584119011378, 1.8157875195671533, 1.8387125935274011, 1.8360730115105124, 1.858144858865177, 1.8621169236127066, 1.8614564918069276, 1.8669150318818937, 1.8748098261216108, 1.8636237918629366, 1.8657487801944506, 1.8651092574175667, 1.8582326058780445]
,[41.19, 55.88, 59.03, 60.71, 62.08, 63.43, 64.91, 66.63, 68.59, 70.66, 72.72, 74.75, 76.49, 77.86, 79.1, 80.0, 80.8, 81.37, 81.77, 81.94, 82.19, 82.23, 82.25, 82.3, 82.1, 81.84, 81.8, 81.44, 81.2, 80.86]
,[50.08, 54.99, 56.83, 57.31, 57.73, 57.93, 57.74, 57.6, 57.35, 57.06, 56.5, 56.24, 55.98, 55.5, 55.16, 55.26, 54.93, 54.91, 54.98, 54.79, 54.9, 54.7, 54.59, 54.69, 54.6, 54.57, 54.52, 54.42, 54.6, 54.57]
]

RNN1024_100 = np.array(RNN1024_100)[:, :25]
GRU1024_100 = np.array(GRU1024_100)[:,:25]
LSTM1024_100 = np.array(LSTM1024_100)[:,:25]
RNN512_100 = np.array(RNN512_100)[:,:25]
GRU512_100 = np.array(GRU512_100)[:,:25]
LSTM512_100 = np.array(LSTM512_100)[:,:25]
RNN1024_50 = np.array(RNN1024_50)[:,:25]
GRU1024_50 = np.array(GRU1024_50)[:,:25]
LSTM1024_50 = np.array(LSTM1024_50)[:,:25]
LSTM2048_100= np.array(LSTM2048_100)[:,:25]

total = [RNN1024_100, GRU1024_100, LSTM1024_100, RNN512_100, GRU512_100, LSTM512_100, RNN1024_50, GRU1024_50, LSTM1024_50]
total1 = [RNN1024_100, LSTM1024_100, RNN512_100, LSTM512_100, RNN1024_50,LSTM1024_50]
total = np.array(total)
total1 = np.array(total1)

title = ["Training Loss","Validation Loss","Traning Accuracy","Validation Accuracy"]
name = ["RNN 1024 100","GRU 1024 100", "LSTM 1024 100",
"RNN 512 100","GRU 512 100", "LSTM 512 100",
"RNN 1024 50","GRU 1024 50", "LSTM 1024 50"
]
name1= ["RNN 1024 100", "LSTM 1024 100",
"RNN 512 100", "LSTM 512 100",
"RNN 1024 50", "LSTM 1024 50"
]
# 4 type of 
for i in range (4) :
	for t in range (6) :
		plt.plot (total1[t,i],color =plt.cm.tab10(t),label = name1[t], alpha= 1.0 )
	
	plt.xlabel('Epoch')
	plt.ylabel('Value')	
	plt.legend(loc='best')
	plt.title (title[i])
	plt.savefig("Comparision"+ title[i]+".png",bbox_inches="tight",dpi=150)
	plt.clf()

print ((total).shape)