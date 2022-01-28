from neuron import h
import neuron
import unittest
import sys
from multiprocessing import Process
try:
    import multiprocessing as mp
    mp.set_start_method('spawn')
except:
    pass

scalar_bistable_data = [4.666144368739553e-24, 2.888704007378294e-23, 1.986504953195841e-22, 1.341708879755938e-21, 8.872570814175589e-21, 5.740880124662921e-20, 3.632196361482038e-19, 2.245604121004388e-18, 1.355711505202327e-17, 7.986451339137754e-17, 4.587323676899676e-16, 2.567045965818926e-15, 1.398326895049450e-14, 7.407949505967670e-14, 3.813250931917600e-13, 1.905347304599457e-12, 9.231798364410461e-12, 4.332732659668245e-11, 1.967471956902693e-10, 8.633990304666386e-10, 3.657079221471421e-09, 1.493207056713948e-08, 5.869401066025243e-08, 2.218029569259474e-07, 8.047212799629250e-07, 2.799213829568570e-06, 9.323183477925731e-06, 2.969562407156739e-05, 9.035408030381566e-05, 2.623954841897339e-04, 7.269141545185255e-04, 1.920726909911178e-03, 4.841879243431064e-03, 1.164965343224173e-02, 2.674863273052559e-02, 5.846777500048252e-02, 1.206799453008834e-01, 2.308459675650935e-01, 3.962758789592548e-01, 5.900229199039158e-01, 7.586218889022415e-01, 8.722981880510015e-01, 9.370823930114011e-01, 9.705058492437171e-01, 9.867204567968444e-01, 9.942426940783661e-01, 9.975977799681778e-01, 9.990359504416327e-01, 9.996249801006252e-01, 9.998477834074035e-01, 9.999041758657206e-01, 9.998477834074035e-01, 9.996249801006252e-01, 9.990359504416326e-01, 9.975977799681777e-01, 9.942426940783655e-01, 9.867204567968437e-01, 9.705058492437160e-01, 9.370823930113995e-01, 8.722981880509845e-01, 7.586218889021992e-01, 5.900229199038706e-01, 3.962758789592359e-01, 2.308459675650852e-01, 1.206799453008814e-01, 5.846777500048142e-02, 2.674863273052497e-02, 1.164965343224158e-02, 4.841879243431020e-03, 1.920726909911166e-03, 7.269141545185224e-04, 2.623954841897313e-04, 9.035408030381501e-05, 2.969562407156726e-05, 9.323183477925702e-06, 2.799213829568569e-06, 8.047212799629269e-07, 2.218029569259469e-07, 5.869401066025247e-08, 1.493207056713951e-08, 3.657079221471437e-09, 8.633990304666446e-10, 1.967471956902691e-10, 4.332732659668252e-11, 9.231798364410503e-12, 1.905347304599471e-12, 3.813250931917631e-13, 7.407949505967741e-14, 1.398326895049453e-14, 2.567045965818940e-15, 4.587323676899705e-16, 7.986451339137816e-17, 1.355711505202341e-17, 2.245604121004394e-18, 3.632196361482056e-19, 5.740880124662959e-20, 8.872570814175665e-21, 1.341708879755951e-21, 1.986504953195844e-22, 2.888704007378305e-23, 4.666144368739581e-24]

trivial_ecs_data = {
False : [1.000000000000000e+00, 9.999975013886804e-01, 9.999774378669442e-01, 9.998977298459814e-01, 9.996832492392076e-01, 9.992330951223182e-01, 9.984342775161091e-01, 9.971750000657639e-01, 9.953548976762590e-01, 9.928916564339932e-01, 9.897243754423555e-01, 9.858143683101370e-01, 9.811441475924241e-01, 9.757152507503439e-01, 9.695454356120868e-01, 9.626656387413414e-01, 9.551169704910168e-01, 9.469479226921377e-01, 9.382118895981384e-01, 9.289650476637475e-01, 9.192646016344460e-01, 9.091673797060952e-01, 8.987287459064514e-01, 8.880017905518656e-01, 8.770367573796769e-01, 8.658806669966089e-01, 8.545770993099358e-01, 8.431661016850746e-01, 8.316841940567001e-01, 8.201644466893430e-01, 8.086366104805101e-01, 7.971272834839320e-01, 7.856601006415908e-01, 7.742559365417961e-01, 7.629331133899011e-01, 7.517076083292696e-01, 7.405932558321451e-01, 7.296019421444131e-01, 7.187437897643434e-01, 7.080273307086645e-01, 6.974596679100502e-01, 6.870466245332152e-01, 6.767928813219394e-01, 6.667021023212317e-01, 6.567770494779278e-01, 6.470196867258985e-01, 6.374312742221647e-01, 6.280124534282580e-01, 6.187633237355973e-01, 6.096835113211366e-01, 6.007722308951912e-01, 5.920283409711493e-01, 5.834503932497362e-01, 5.750366766708355e-01, 5.667852566452943e-01, 5.586940099388136e-01, 5.507606556408047e-01, 5.429827826135633e-01, 5.353578737816238e-01, 5.278833275879240e-01, 5.205564769125375e-01, 5.133746057212193e-01, 5.063349636848303e-01, 4.994347789867492e-01, 4.926712695135610e-01, 4.860416526044784e-01, 4.795431535169798e-01, 4.731730127498988e-01, 4.669284923505265e-01, 4.608068813190689e-01, 4.548055002118984e-01, 4.489217050343421e-01, 4.431528905041363e-01, 4.374964927580476e-01, 4.319499915664357e-01, 4.265109121135835e-01, 4.211768263954196e-01, 4.159453542806875e-01, 4.108141642766345e-01, 4.057809740358395e-01, 4.008435506368045e-01, 3.959997106673694e-01, 3.912473201368166e-01, 3.865842942396779e-01, 3.820085969917059e-01, 3.775182407561858e-01, 3.731112856767305e-01, 3.687858390308746e-01, 3.645400545171554e-01, 3.603721314869148e-01, 3.562803141307546e-01, 3.522628906284160e-01, 3.483181922698216e-01, 3.444445925540838e-01, 3.406405062724689e-01, 3.369043885805584e-01, 3.332347340641985e-01, 3.296300758032397e-01, 3.260889844365475e-01, 3.226100672312980e-01, 3.191919671591613e-01],
1e-2 : [1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 9.999999999993757e-01, 9.999999999948940e-01, 9.999999999684935e-01, 9.999999997476527e-01, 9.999999928933891e-01, 9.999999611564773e-01, 9.999998797767268e-01, 9.999996998881439e-01, 9.999993374567406e-01, 9.999984853833063e-01, 9.999969740580184e-01, 9.999944882384333e-01, 9.999906315949002e-01, 9.999849509581277e-01, 9.999769206381147e-01, 9.999582122018814e-01, 9.999297152881566e-01, 9.998885520830283e-01, 9.998315279906250e-01, 9.996818635176246e-01, 9.994522087548142e-01, 9.991215537513162e-01, 9.986688188930973e-01, 9.980737640971513e-01, 9.973169807955987e-01, 9.963810719470240e-01, 9.952501731850908e-01, 9.939108695612021e-01, 9.923517494756579e-01, 9.905637628430480e-01, 9.885402079276301e-01, 9.862765182499404e-01, 9.837701825345700e-01, 9.810207339243457e-01, 9.780291325292961e-01, 9.747989764630028e-01, 9.713343413784561e-01, 9.676399370118218e-01, 9.610664511514549e-01, 9.539287981952346e-01, 9.462557577837218e-01, 9.380908351569157e-01, 9.295048630242134e-01, 9.272938750650753e-01, 9.250579717830375e-01, 9.227970935555948e-01, 9.164665386395120e-01, 9.099911643711576e-01, 9.033621457398684e-01, 8.966076655702790e-01, 8.897506341031615e-01, 8.827836396691656e-01, 8.757430253325005e-01, 8.686235564317917e-01, 8.614266253287830e-01, 8.541863694365750e-01, 8.468993821627302e-01, 8.395705411285332e-01, 8.322240727554534e-01, 8.248512178596673e-01, 8.174717412805539e-01, 8.101012803444277e-01, 8.027295128188973e-01, 7.953825709154709e-01, 7.880520562892473e-01, 7.807347758450052e-01, 7.734449586695845e-01, 7.661975818078829e-01, 7.589799271053987e-01, 7.518171027867613e-01, 7.446977692754075e-01, 7.376160661891280e-01, 7.305954685595947e-01, 7.236266087629475e-01, 7.167068363568081e-01, 7.140993659912696e-01, 7.115003569118910e-01, 7.053989759515575e-01, 6.937157033233743e-01, 6.892286429728892e-01, 6.847738597587193e-01, 6.803460439703601e-01, 6.736943892201644e-01, 6.671180984390447e-01, 6.622364244386257e-01, 6.573969190766189e-01, 6.525933207264888e-01, 6.478347504056896e-01, 6.431166994633450e-01, 6.384369407276960e-01, 6.290516157893640e-01, 6.198222188748919e-01, 6.175428045973979e-01, 6.152735585854211e-01, 6.111170811451881e-01, 6.031212236479893e-01, 5.952593539110380e-01, 5.921305074751056e-01, 5.890215438866859e-01, 5.843049294344698e-01, 5.796335966290896e-01, 5.750160381540556e-01, 5.704420016665088e-01, 5.659178450605010e-01, 5.614455518912613e-01, 5.591788148460601e-01, 5.569248279174298e-01, 5.506074431743505e-01, 5.478382336868175e-01, 5.450878675391179e-01, 5.387888979310328e-01, 5.362404523147913e-01, 5.337094641666161e-01, 5.282374991972423e-01, 5.259248454152894e-01, 5.236262814879684e-01, 5.182614254027890e-01, 5.158555312376837e-01, 5.134660721930772e-01, 5.077709278344216e-01, 5.053179820104490e-01, 5.028817741515068e-01, 4.974407642335685e-01, 4.952012718592664e-01, 4.929770110443390e-01, 4.880637159524582e-01, 4.859684632733423e-01, 4.838861488391641e-01, 4.790294758699501e-01, 4.768706516921771e-01, 4.747266903353097e-01, 4.696849124915995e-01, 4.675266380099869e-01, 4.653827515562493e-01, 4.605962240576634e-01, 4.586085068420688e-01, 4.566341643693850e-01, 4.522282618718538e-01, 4.503369915407668e-01, 4.484573583607938e-01, 4.440766399922996e-01, 4.421436521416536e-01, 4.402239033770282e-01, 4.357529446279363e-01, 4.338466468392896e-01, 4.319526749076715e-01, 4.277194009540304e-01, 4.259480291942094e-01, 4.241883948256027e-01, 4.202300998848154e-01, 4.185239108263153e-01, 4.168280792217872e-01, 4.128821814385824e-01, 4.111518412231812e-01, 4.094332017859506e-01, 4.054591322790473e-01, 4.037685048369686e-01, 4.020884387112946e-01, 3.983255882607288e-01, 3.967407957791139e-01, 3.951663235196693e-01, 3.916025661686941e-01, 3.900627879901100e-01, 3.885321706996029e-01, 3.849784483567140e-01, 3.834281028668022e-01, 3.818880643760414e-01, 3.783453864220350e-01, 3.768397186025170e-01, 3.753431216105738e-01, 3.719827243333056e-01, 3.705596473485314e-01, 3.691456730437073e-01, 3.659301712184497e-01, 3.645393288417587e-01, 3.631565593836533e-01, 3.599538911939479e-01, 3.585625234903733e-01, 3.571802315061479e-01, 3.540119540790766e-01, 3.526654577087503e-01, 3.513267792978637e-01, 3.483128923342382e-01, 3.470307463292109e-01, 3.457566587669847e-01, 3.428492728471916e-01, 3.415914251565042e-01, 3.403406775305906e-01, 3.374508890138111e-01, 3.361995660265230e-01, 3.349562467114465e-01, 3.321133636377239e-01, 3.309044582572311e-01, 3.297023177240813e-01, 3.269887097799309e-01, 3.258300483601927e-01, 3.246785486404988e-01, 3.220444676004350e-01, 3.209052709642934e-01, 3.197723133954909e-01],
1e-5 : [1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 1.000000000000000e+00, 9.999999999999994e-01, 9.999999999999730e-01, 9.999999999998286e-01, 9.999999999994353e-01, 9.999999999985202e-01, 9.999999999965848e-01, 9.999999999914210e-01, 9.999999999815654e-01, 9.999999999642780e-01, 9.999999999357950e-01, 9.999999998244792e-01, 9.999999995977931e-01, 9.999999987558622e-01, 9.999999969054565e-01, 9.999999933717028e-01, 9.999999871894636e-01, 9.999999770945371e-01, 9.999999615055236e-01, 9.999999384936957e-01, 9.999999057511308e-01, 9.999998222204165e-01, 9.999996889877317e-01, 9.999994874837332e-01, 9.999991954947148e-01, 9.999987869759613e-01, 9.999978778927705e-01, 9.999965094234943e-01, 9.999945377974357e-01, 9.999917976154713e-01, 9.999881018395195e-01, 9.999832421044147e-01, 9.999769893073577e-01, 9.999690944252573e-01, 9.999592894153977e-01, 9.999401848217710e-01, 9.999149868024271e-01, 9.998825523031706e-01, 9.998416677700163e-01, 9.997910595925650e-01, 9.997294043565842e-01, 9.996553389790078e-01, 9.995674703998642e-01, 9.994643850266534e-01, 9.993446578768627e-01, 9.992068613208905e-01, 9.990495732666037e-01, 9.988713847467867e-01, 9.986709069016458e-01, 9.984467774204933e-01, 9.981976664056399e-01, 9.979222816859891e-01, 9.976193735296895e-01, 9.972877388222079e-01, 9.969262246907040e-01, 9.965337316535895e-01, 9.961092162612745e-01, 9.956516933110915e-01, 9.951602375882754e-01, 9.946339852520572e-01, 9.940721347818040e-01, 9.934739476574072e-01, 9.928387486091628e-01, 9.921659257085935e-01, 9.914549300099351e-01, 9.907052751686757e-01, 9.899165365560477e-01, 9.890883505198331e-01, 9.882204130401707e-01, 9.873124787412751e-01, 9.863643591446407e-01, 9.853759215358775e-01, 9.843470868593674e-01, 9.832778285388312e-01, 9.821681700449177e-01, 9.810181837626457e-01, 9.798279882517430e-01, 9.785977472491776e-01, 9.773276666309043e-01, 9.760179936330398e-01, 9.746690135131258e-01, 9.732810490694735e-01, 9.718544574219034e-01, 9.703896283469345e-01, 9.688869823629818e-01, 9.662560899379753e-01, 9.635203094788860e-01, 9.606821993784824e-01, 9.577444920821762e-01, 9.547100690698106e-01, 9.515819411387303e-01, 9.483632227783803e-01, 9.450571205528219e-01, 9.416669021033438e-01, 9.381959001044843e-01, 9.346474739566473e-01, 9.310250020056358e-01, 9.273318651957428e-01, 9.235714575597201e-01, 9.197471440818522e-01, 9.158622774784529e-01, 9.119201741214706e-01, 9.079241164053400e-01, 9.038773101206564e-01, 8.997829152782374e-01, 8.956440506961761e-01, 8.914637634840353e-01, 8.872450198327338e-01, 8.829907105217275e-01, 8.787036576363941e-01, 8.707492329602121e-01, 8.687467373185769e-01, 8.667391783027991e-01, 8.647268019171629e-01, 8.627098501557753e-01, 8.585978518951599e-01, 8.544698540634895e-01, 8.503277143709528e-01, 8.461732532471191e-01, 8.420082065243172e-01, 8.378342644577640e-01, 8.336530592572513e-01, 8.294661714342418e-01, 8.252750957681314e-01, 8.210812733406646e-01, 8.168861006274361e-01, 8.126909233407180e-01, 8.084970284424999e-01, 8.018705279973948e-01, 7.952548736797830e-01, 7.886543612921902e-01, 7.820730077033664e-01, 7.755145256970315e-01, 7.689823477006539e-01, 7.624796584457091e-01, 7.560093783176929e-01, 7.495742104755058e-01, 7.431766425064636e-01, 7.368189634231701e-01, 7.305032400696735e-01, 7.242313466189446e-01, 7.180049652774664e-01, 7.118256479784464e-01, 7.056948260292686e-01, 7.032583361895295e-01, 7.008298605278855e-01, 6.984094704872370e-01, 6.959972341046202e-01, 6.935932152404094e-01, 6.889317430774708e-01, 6.817668350489530e-01, 6.746798127752269e-01, 6.676718057412527e-01, 6.607437322115557e-01, 6.538963343303841e-01, 6.471301405820917e-01, 6.404455883106537e-01, 6.387872416184449e-01, 6.371340113850150e-01, 6.354859019542481e-01, 6.323179670207283e-01, 6.291691359105558e-01, 6.243492415503886e-01, 6.195747895117473e-01, 6.148457081070352e-01, 6.101619207395151e-01, 6.055232995385412e-01, 6.009296920940354e-01, 5.963809255739797e-01, 5.884265027623434e-01, 5.806112287097513e-01, 5.729337321255051e-01, 5.653924575507177e-01, 5.579857024351769e-01, 5.561548261765027e-01, 5.543322219963571e-01, 5.525178614099090e-01, 5.497619521958399e-01, 5.470251014183799e-01, 5.421958421339816e-01, 5.374261214332550e-01, 5.327153071018452e-01, 5.280627574108234e-01, 5.234678232248013e-01, 5.189298444469039e-01, 5.144481596152644e-01, 5.100220936678099e-01, 5.056509822776560e-01, 5.013341346033774e-01, 4.970708987429328e-01, 4.928605836118120e-01, 4.887024961805134e-01, 4.845959781161491e-01, 4.805403497251276e-01, 4.765349346341766e-01, 4.725790728234394e-01, 4.686720914229373e-01, 4.648133480441644e-01, 4.610021778781840e-01, 4.572379175659361e-01, 4.535199244031417e-01, 4.498475710369739e-01, 4.462202101246375e-01, 4.426372375753840e-01, 4.390980179451507e-01, 4.356019205688260e-01, 4.321483548727800e-01, 4.287367136802313e-01, 4.253663991812640e-01, 4.220368327619753e-01, 4.187474280885136e-01, 4.154976300176047e-01, 4.122868660369579e-01, 4.091145681113114e-01, 4.043631518312791e-01, 3.996975359393022e-01, 3.951158478794149e-01, 3.906162701651016e-01, 3.861970390711226e-01, 3.841086119708872e-01, 3.820380229719526e-01, 3.799850857201517e-01, 3.779496187391600e-01, 3.745426919402392e-01, 3.711844377457629e-01, 3.678740151738357e-01, 3.646106065243293e-01, 3.613933918170190e-01, 3.582215709845467e-01, 3.550943187555968e-01, 3.520108594211252e-01, 3.489704836755959e-01, 3.459724290685680e-01, 3.430159438599149e-01, 3.401003272980346e-01, 3.372248857211048e-01, 3.343889511711801e-01, 3.315918392385992e-01, 3.288328612250609e-01, 3.261113573130471e-01, 3.234267379284118e-01, 3.207783627593125e-01]
}

def scalar_bistable():
    from neuron import rxd
    h.load_file('stdrun.hoc')
    s = h.Section(name='s')
    s.nseg = 101
    cyt = rxd.Region(h.allsec())
    c = rxd.Species(cyt, name='c', initial=lambda node: 1 if 0.4 < node.x < 0.6 else 0, d=1)
    r = rxd.Rate(c, -c * (1-c)*(0.3-c))
    h.finitialize()
    h.run()

    #check the results
    result = h.Vector(c.nodes.concentration)
    cmpV = h.Vector(scalar_bistable_data)
    cmpV.sub(result)
    cmpV.abs()
    if cmpV.sum() < 1e-6:
        sys.exit(0) 
    sys.exit(-1)

def trivial_ecs(scale):
    from neuron import h, crxd as rxd
    import numpy
    import warnings
    warnings.simplefilter("ignore", UserWarning)
    h.load_file('stdrun.hoc')
    tstop = 10
    if scale:   #variable step case
        h.CVode().active(True)
        h.CVode().event(tstop)
    else:           #fixed step case
        h.dt = 0.1

    sec = h.Section() #NEURON requires at least 1 section

    # enable extracellular RxD
    rxd.options.enable.extracellular = True

    # simulation parameters
    dx = 1.0    # voxel size
    L = 9.0     # length of initial cube
    Lecs = 21.0 # lengths of ECS

    # define the extracellular region
    extracellular = rxd.Extracellular(-Lecs/2., -Lecs/2., -Lecs/2.,
                                      Lecs/2., Lecs/2., Lecs/2., dx=dx,
                                      volume_fraction=0.2, tortuosity=1.6)

    # define the extracellular species
    k_rxd = rxd.Species(extracellular, name='k', d=2.62, charge=1,
                        atolscale=scale, initial=lambda nd: 1.0 if 
                        abs(nd.x3d) <= L/2. and abs(nd.y3d) <= L/2. and 
                        abs(nd.z3d) <= L/2. else 0.0)

    # record the concentration at (0,0,0)
    ecs_vec = h.Vector()
    ecs_vec.record(k_rxd[extracellular].node_by_location(0, 0, 0)._ref_value)
    h.finitialize()
    h.continuerun(tstop) #run the simulation
    
    # compare with previous solution 
    ecs_vec.sub(h.Vector(trivial_ecs_data[scale]))
    ecs_vec.abs()
    if ecs_vec.sum() > 1e-9:
        return -1
    return 0
    

class RxDTestCase(unittest.TestCase):
    """Tests of rxd"""

    def test_rxd(self):
        p = Process(target=scalar_bistable)
        p.start()
        p.join()
        assert(p.exitcode == 0)
        return 0 

    def test_ecs_diffusion_fixed_step(self):
        p = Process(target=trivial_ecs, args=(False,))
        p.start()
        p.join()
        assert(p.exitcode == 0)
        return 0  

    def test_ecs_diffusion_variable_step_coarse(self):
        p = Process(target=trivial_ecs, args=(1e-2,))
        p.start()
        p.join()
        assert(p.exitcode == 0)
        return 0 

    def test_ecs_diffusion_variable_step_fine(self):
        p = Process(target=trivial_ecs, args=(1e-5,))
        p.start()
        p.join()
        assert(p.exitcode == 0)
        return 0 


def suite():
    suite = unittest.makeSuite(RxDTestCase,'test')
    return suite
    
def test():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

if __name__ == "__main__":
    # unittest.main()
    test()
