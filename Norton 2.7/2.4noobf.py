def startNorton():

    n = 0
    boost = 1
    add = 1

    tables = {
        'weapons': {
            'AR': {
                'mode': 'auto',
                'cdif': False,
                'firerate': 0.1329,
                'pattern': [
                    (1.390706, -2.003941), (1.176434, -3.844176), (3.28, -5.46), (5, -7), (5.094189, -8.342467), (4.426013, -9.487704), (3.250455, -10.44915), (1.73545, -11.22279), (0.04893398, -11.8046), [-1.641158, -12.19056], [-3.166891, -12.58713], [-4.360331, -13.32077], [-5.053545, -14.32128], [-5.090651, -15.51103], [-4.489915, -16.81242], [-3.382552, -18.14783], [-1.899585, -19.43966], [-0.1720295, -20.61031], [1.669086, -21.58213], [3.492748, -22.27755], [5.16793, -22.61893], [6.563614, -22.81778], [7.548776, -23.37389], [7.992399, -24.21139], [7.512226, -25.23734], [6.063792, -26.35886], [4.117367, -27.48302], [2.143932, -28.51692], [0.6144824, -29.36766]
                ],
                'ct': [
                     (121.9615), (92.6334), (138.6060), (113.3788), (66.2515), 66.2953, 75.9328, 85.0552, 89.2026, 86.6802, 78.8214, 70.0451, 75, 75, 71.6676, 86.7409, 98.3364, 104.3413, 104.0932, 97.5877, 85.4806, 75, 75, 75, 75, 91.5937, 112.3867, 111.3935, 87.5067, 10000
                ],
                'mag': 30
            },
             'LR': {
                'mode': 'auto',
                'cdif': False,
                'firerate': 0.115,
                'pattern': [
                    [0.09836517, -1.004928], [0.3469534, -2.248523], [0.7512205, -3.575346], [1.326888, -4.829963], [1.958069, -5.858609], [2.527623, -6.687347], [2.918412, -7.399671], [3.007762, -8.005643], [2.641919, -8.515327], [1.950645, -8.938788], [1.144313, -9.286088], [0.4332969, -9.567291], [0.02797037, -9.793953], [0.04550591, -9.992137], [0.2685102, -10.17017], [0.6408804, -10.33037], [1.127565, -10.47505], [1.693516, -10.60654], [2.303682, -10.72716], [2.923013, -10.83923], [3.516459, -10.94506], [4.04897, -11.04699], [4.485496, -11.14732], [4.790986, -11.24838], [4.92656, -11.35249], [4.387823, -11.46197], [3.16274, -11.57914], [1.714368, -11.70632], [0.5057687, -11.84584]
                ],
                'ct': [
                    50.4865, 63.4098, 69.3522, 69.0191, 60.3428, 50.2792, 40.6239, 30.6262, 31.3695, 40.5333, 43.8973, 38.2302, 23.2199, 9.9479, 14.2676, 20.2684, 25.3868, 29.0513, 31.0987, 31.4694, 30.1404, 27.1089, 22.3954, 16.0886, 8.5469, 27.4875, 61.5337, 72.6973, 60.8312
                ],
                'mag': 30
            },
            'MP5': {
                'mode': 'auto',
                'cdif': False,
                'firerate': 0.095,
                'pattern': [
                    [0, -0.8688382], [0, -2.042219], [-2.992364e-14, -3.370441], [-0.5103882, -4.703804], [-1.687297, -5.892606], [-2.999344, -6.787148], [-3.915147, -7.311441], [-3.948318, -7.742482], [-3.224567, -8.127406], [-2.228431, -8.468721], [-1.438722, -8.768936], [-1.288914, -9.03056], [-1.598686, -9.2561], [-2.154637, -9.448063], [-2.826861, -9.60896], [-3.485454, -9.741299], [-4.000507, -9.847586], [-4.242117, -9.930332], [-4.184897, -9.992043], [-3.969568, -10.03523], [-3.629241, -10.0624], [-3.194572, -10.07606], [-2.696223, -10.07872], [-2.16485, -10.07288], [-1.631112, -10.06106], [-1.125667, -10.04577], [-0.6791761, -10.02951], [-0.3222946, -10.01479], [-0.08568263, -10.00412]
                ],
                'ct': [
                        41113.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426
                    ],
                'mag': 30
            },
            'TH': {
                'mode': 'auto',
                'cdif': False,
                'firerate': 0.125,
                'pattern': [
                    [0.7399524, -1.565956], [1.011324, -3.109221], [0.8437103, -4.587918], [0.3127854, -5.960169], [-0.3338249, -7.184096], [-0.8446444, -8.217823], [-0.9689822, -9.093672], [-0.6067921, -9.877484], [0.01632042, -10.57721], [0.6324611, -11.20081], [0.9737339, -11.75624], [0.8438975, -12.25145], [0.3745165, -12.6944], [-0.2263549, -13.09305], [-0.7514643, -13.45534], [-0.9935587, -13.78924], [-0.862007, -14.1027], [-0.5397906, -14.40368], [-0.1962007, -14.70013]
                ],
                'ct': [
                        4113.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426
                    ],
                'mag': 20
            },
            'CU': {
                'mode': 'auto',
                'cdif': False,
                'firerate': 0.095,
                'pattern': [
                    [0.6512542, -1.305408], [0.9681615, -2.599905], [0.9872047, -3.859258], [0.6951124, -5.05923], [0.2062594, -6.175588], [-0.3338249, -7.184096], [-0.7796098, -8.060521], [-0.9855663, -8.812342], [-0.8372459, -9.496586], [-0.4148501, -10.11968], [0.1267298, -10.68622], [0.6324611, -11.20081], [0.9473124, -11.66807], [0.9353167, -12.09258], [0.6385964, -12.47896], [0.1786009, -12.83181], [-0.3247314, -13.15574], [-0.7514643, -13.45534], [-0.9816588, -13.73522], [-0.9354943, -13.99999], [-0.714118, -14.25425], [-0.4193012, -14.5026], [-0.1487077, -14.74965]
                ],
                'ct': [
                        40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426
                    ],
                'mag': 24
            },
            'SAR': {
                'mode': 'semi',
                'cdif': True,
                'firerate': 0.123,
                'pattern': [
                    [0.0, -3.25], [0.0, -6.5], [0.0, -9.75], [0.0, -13.0], [0.0, -16.25], [0.0, -19.5], [0.0, -22.75], [0.0, -26.0], [0.0, -29.25], [0.0, -32.5], [0.0, -35.75], [0.0, -39.0], [0.0, -42.25], [0.0, -45.5], [0.0, -48.75], [0.0, -52.0]
                ],
                'ct': [
                        40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426
                    ],
                'mag': 16
            },
            'M2': {
                'mode': 'auto',
                'cdif': True,
                'firerate': 0.115,
                'pattern': [
                    [0.0, -2.75], [0.0, -5.5], [0.0, -8.25], [0.0, -11.0], [0.0, -13.75], [0.0, -16.5], [0.0, -19.25], [0.0, -22.0], [0.0, -24.75], [0.0, -27.5], [0.0, -30.25], [0.0, -33.0], [0.0, -35.75], [0.0, -38.5], [0.0, -41.25], [0.0, -44.0], [0.0, -46.75], [0.0, -49.5], [0.0, -52.25], [0.0, -55.0], [0.0, -57.75], [0.0, -60.5], [0.0, -63.25], [0.0, -66.0], [0.0, -68.75], [0.0, -71.5], [0.0, -74.25], [0.0, -77.0], [0.0, -79.75], [0.0, -82.5], [0.0, -85.25], [0.0, -88.0], [0.0, -90.75], [0.0, -93.5], [0.0, -96.25], [0.0, -99.0], [0.0, -101.75], [0.0, -104.5], [0.0, -107.25], [0.0, -110.0], [0.0, -112.75], [0.0, -115.5], [0.0, -118.25], [0.0, -121.0], [0.0, -123.75], [0.0, -126.5], [0.0, -129.25], [0.0, -132.0], [0.0, -134.75], [0.0, -137.5], [0.0, -140.25], [0.0, -143.0], [0.0, -145.75], [0.0, -148.5], [0.0, -151.25], [0.0, -154.0], [0.0, -156.75], [0.0, -159.5], [0.0, -162.25], [0.0, -165.0], [0.0, -167.75], [0.0, -170.5], [0.0, -173.25], [0.0, -176.0], [0.0, -178.75], [0.0, -181.5], [0.0, -184.25], [0.0, -187.0], [0.0, -189.75], [0.0, -192.5], [0.0, -195.25], [0.0, -198.0], [0.0, -200.75], [0.0, -203.5], [0.0, -206.25], [0.0, -209.0], [0.0, -211.75], [0.0, -214.5], [0.0, -217.25], [0.0, -220.0], [0.0, -222.75], [0.0, -225.5], [0.0, -228.25], [0.0, -231.0], [0.0, -233.75], [0.0, -236.5], [0.0, -239.25], [0.0, -242.0], [0.0, -244.75], [0.0, -247.5], [0.0, -250.25], [0.0, -253.0], [0.0, -255.75], [0.0, -258.5], [0.0, -261.25], [0.0, -264.0], [0.0, -266.75], [0.0, -269.5], [0.0, -272.25], [0.0, -275.0], [0.0, -277.75]
                 ],
                'ct': [
                        40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426, 40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426, 40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426, 40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426, 40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416, 70009.3989, 52.7631, 2001.6158, 4000.9873, 5002.6494, 4002.2424, 1500.0739, 1900.1590, 2900.4080, 3400.5606, 3300.5879, 2600.2953, 120.7693, 400.2078, 1000.9808, 1070.0705, 1000.7442, 2400.9178, 2600.5703, 2600.6934, 2500.2838, 2200.3394, 1700.8592, 1100.8426, 40003.4419, 50008.6690, 60006.4111, 71000.3855, 80000.6416

                    ],
                'mag': 100
            },
            'PYT': {
                'mode': 'semi',
                'cdif': True,
                'firerate': 0.001,
                'pattern': [
                    [0.0, -8.0], [0.0, -16.0], [0.0, -24.0], [0.0, -32.0], [0.0, -40.0], [0.0, -48.0], [0.0, -56.0]
                ],
                'mag': 6
            }
        },
        'sight': {
            'iron': 1,
            'holo': 1.18605,
            '8': 3.83721,
            'simple': 0.8
            },
        'att': {
            'none': 1,
            'silencer': 0.8,
            'boost': 0.9,
            'brake': 0.5
            }
    }

    main = Tk()
    main.geometry("200x340+50+50")
    main.configure(bg="white")
    main.title("")
    main.lift()
    main.resizable(0,0)
    main.iconbitmap('norton.ico')

    active = True
    C = 100
    cW = 'Assault Rifle'
    cA = 'None'
    cS = 'Iron'
    rMode = 'Rage'
    antiafk = False
    ran = 0
    nonads = False

    awd = Label(main, text=f"Active: {active}")
    awd.place(x=10,y=10)
    lC = Label(main, text=f"Control: {C}%")
    lC.place(x=10,y=40)

    wepon = Label(main, text=f"Weapon: {cW}")
    wepon.place(x=10,y=70)

    scop = Label(main, text=f"Sight: {cS}")
    scop.place(x=10,y=100)

    atta = Label(main, text=f"Attatchment: {cA}")
    atta.place(x=10,y=130)

    rbl = Label(main, text=f"Recoil Mode: {rMode}")
    rbl.place(x=10,y=160)

    aal = Label(main, text=f"Anti-AFK [BETA]: {antiafk}")
    aal.place(x=10,y=190)

    sensl = Label(main, text=f"In-game sens: {sens}")
    sensl.place(x=10,y=220)

    fovl = Label(main, text=f"In-game FOV: {fov}")
    fovl.place(x=10,y=250)

    ral = Label(main, text=f"Randomization: {ran}")
    ral.place(x=10,y=280)

    hip = Label(main, text=f"Hip Control: {nonads}")
    hip.place(x=10,y=310)

    disc = Label(main, text=r"HVw6kY6", bg="white",fg="#DBDBDB")
    disc.place(x=133,y=315)

    userlabel = Label(main, text="v2.7", bg="white",fg="#DBDBDB")
    userlabel.place(x=135,y=300)

    def leftDown(): 
        lmb_state = win32api.GetKeyState(0x01)
        return lmb_state < 0

    def rightDown():
        rmb_state = win32api.GetKeyState(0x02)
        return rmb_state < 0

    def ctrlDown():
        ctrl_state = win32api.GetKeyState(0x11)
        return ctrl_state < 0


    wep = tables['weapons']['AR']

    lastShot = (0, 0)
    fr = wep['firerate']

    sa = False
    tapS = True
    show = True

    mult = (-0.03 * ((sens * 3) * (fov / 100)))

    scope = 1
    AAK = 'w'
    antiafk = False
    offsetm2 = 1
    shot = 1
    
    if oldbinds == 0:
        while True:
            main.update()
            if keyboard.is_pressed('r'):
                if sa == True:
                    shot = 1
                    n = 0
            if keyboard.is_pressed('shift + down arrow'):
                if C > 4:
                    C -= 5
                    lC.destroy()
                    lC = Label(main, text=f"Control: {C}%")
                    lC.place(x=10,y=40)
                    time.sleep(0.1)
                else:
                    C = 5
            if keyboard.is_pressed('shift + up arrow'):
                if C < 100:
                    C += 5
                    lC.destroy()
                    lC = Label(main, text=f"Control: {C}%")
                    lC.place(x=10,y=40)
                    time.sleep(0.05)
                else:
                    C = 100
            if win32api.GetAsyncKeyState(rl)<0:
                if rMode == 'Rage':
                    rMode = 'Legit'
                else:
                    rMode = 'Rage'
                rbl.destroy()
                rbl = Label(main, text=f"Recoil Mode: {rMode}")
                rbl.place(x=10,y=160)
                time.sleep(0.2)
            if keyboard.is_pressed('shift + left arrow'):
                if ran > 0:
                    ran -= 1
                    ral.destroy()
                    ral = Label(main, text=f"Randomization: {ran}")
                    ral.place(x=10,y=280)
                    time.sleep(0.1)
                else:
                    ran = 1
            if keyboard.is_pressed('shift + right arrow'):
                if ran < 10:
                    ran += 1
                    ral.destroy()
                    ral = Label(main, text=f"Randomization: {ran}")
                    ral.place(x=10,y=280)
                    time.sleep(0.1)
                else:
                    ran = 10
            if keyboard.is_pressed('shift + f3'):
                if show == True:
                    main.withdraw()
                    show = False
                    time.sleep(0.2)
                else:
                    main.deiconify()
                    show = True
                    time.sleep(0.2)
            if win32api.GetAsyncKeyState(tog)<0:
                if active == False:
                    active = True
                    time.sleep(0.2)
                else:
                    active = False
                    time.sleep(0.2)
                awd.destroy()
                awd = Label(main, text=f"Active: {active}")
                awd.place(x=10,y=10)
            if antiafk == True:
                keyboard.press(AAK)
                keyboard.release(AAK)
                cd(30)
                if AAK == 'w':
                    AAK = 'a'
                elif AAK == 'a':
                    AAK = 's'
                elif AAK == 's':
                    AAK = 'd'
                elif AAK == 'd':
                    AAK = 'w'
            if ctrlDown():
                crouch = 0.5
            else:
                crouch = 1
            if win32api.GetAsyncKeyState(hipk)<0:
                if nonads == True:
                    nonads = False
                else:
                    nonads = True
                hip.destroy()
                hip = Label(main, text=f"Hip Control: {nonads}")
                hip.place(x=10,y=310)
                time.sleep(0.2)
            if win32api.GetAsyncKeyState(iron)<0:
                scope = 1
                cS = 'Iron'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if win32api.GetAsyncKeyState(eigh)<0:
                scope = 3.83721
                cS = '8x'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if win32api.GetAsyncKeyState(holo)<0:
                scope = 1.18605
                cS = 'Holosight'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if win32api.GetAsyncKeyState(simp)<0:
                scope = 0.8
                cS = 'Simple'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if win32api.GetAsyncKeyState(boos)<0:
                boost = 0.9
                add = 1
                cA = 'Muzzle Boost'
                atta.destroy()
                atta = Label(main, text=f"Attatchment: {cA}")
                atta.place(x=10,y=130)
            if win32api.GetAsyncKeyState(sile)<0:
                boost = 1
                add = 0.8
                cA = 'Silencer'
                atta.destroy()
                atta = Label(main, text=f"Attatchment: {cA}")
                atta.place(x=10,y=130)
            if win32api.GetAsyncKeyState(none)<0:
                boost = 1
                add = 1
                cA = 'None'
                atta.destroy()
                atta = Label(main, text=f"Attatchment: {cA}")
                atta.place(x=10,y=130)
            if win32api.GetAsyncKeyState(m2)<0:
                wep = tables['weapons']['M2']
                wepon.destroy()
                cW = 'M249'
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if win32api.GetAsyncKeyState(lr)<0:
                wep = tables['weapons']['LR']
                cW = 'LR-300'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if win32api.GetAsyncKeyState(mp5)<0:
                wep = tables['weapons']['MP5']
                cW = 'MP5A4'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if win32api.GetAsyncKeyState(ak)<0:
                wep = tables['weapons']['AR']
                cW = 'Assault Rifle'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if win32api.GetAsyncKeyState(sar)<0:
                wep = tables['weapons']['SAR']
                cW = 'Semi'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if win32api.GetAsyncKeyState(cu)<0:
                wep = tables['weapons']['CU']
                cW = 'Custom SMG'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if win32api.GetAsyncKeyState(th)<0:
                wep = tables['weapons']['TH']
                cW = 'Thompson'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if nonads == True:
                if leftDown():
                    if not rightDown():
                        for recoil in wep['pattern']:
                            fr = wep['firerate']
                            if rightDown():
                                nads = scope * add
                                
                            else:
                                
                                if wep == tables['weapons']['AR']:
                                    nads = 0.61
                                elif wep == tables['weapons']['LR']:
                                    nads = 0.63
                                elif wep == tables['weapons']['MP5']:
                                    nads = 0.63
                            
                            dx = ((recoil[0] - lastShot[0]) / mult) * nads
                            dy = ((recoil[1] - lastShot[1]) / mult) * nads
                                    
                            s = time.time()
                            end = s + fr
                            moved = (0, 0)
                            while (time.time() < end):
                                t = (time.time() - s) / fr
                                b = max(min(t, 1.0), 0.0)
                                x = math.floor((dx * b) - moved[0])
                                y = math.floor((dy * b) - moved[1])

                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)

                                moved = tuple(map(operator.add, moved, (x, y)))
                                time.sleep(1 / 1000)

                            dx = dx - moved[0]
                            dy = dy - moved[1]



                            lastShot = recoil
                            if leftDown():
                                continue
                            else:
                                lastShot = (0,0)
                                break
                else:
                    shot = 1
                    lastShot = (0, 0)
                    
            if leftDown() and rightDown():
                if active == True:
                    for recoil in wep['pattern']:
                        doingads = True
                        fr = wep['firerate']
                        if shot < (wep['mag'] + xyz):
                            shot += 1
                            if wep['cdif'] == True:
                                offset = crouch
                                if offset == 0.5:
                                    if wep == tables['weapons']['M2']:
                                        offsetm2 = 0.98
                                    if wep == tables['weapons']['M2']:
                                        offsetm2 = 1
                                else:
                                    offsetm2 = 0.95
                            else:
                                offset = 1
                                offsetm2 = 1
                            if ran == 0:
                                rxm = 1
                                rym = 1
                            else:
                                rxm = (random.randrange((100 - ran), (100 + ran)) / 100)
                                rym = (random.randrange((100 - ran), (100 + ran)) / 100)
                            if rMode == 'Rage':
                                if wep == tables['weapons']['AR'] or tables['weapons']['LR']:
                                    ct = (wep['ct'][n]) / 1000
                                    if ct > wep['firerate']:
                                        fr = wep['firerate']
                                        wait = 0
                                    else:
                                        wait = wep['firerate'] - ct
                                        fr = wep['firerate'] - wait

                                else:
                                    fr = wep['firerate']
                                    wait = 0
                            else:
                                fr = wep['firerate']
                                wait = 0

                            if rMode == 'Rage':
                                n += 1
                                if wep == tables['weapons']['AR']:
                                    if n > 10:
                                        fr = fr + 0.01
                                        wait = wait - 0.01
                                if wep == tables['weapons']['LR']:
                                    if n > 5:
                                        fr = 0.1
                                        wait = 0.015
                            if cW == 'Custom SMG':
                                if cS == 'Iron':
                                    smgoff = 0.8
                                else:
                                    smgoff = 1
                            elif cW == 'Thompson':
                                if cS == 'Iron':
                                    smgoff = 0.8
                                else:
                                    smgoff = 1
                            else:
                                smgoff = 1
                            if nonads == True:
                                if leftDown():
                                    dads = 0.61
                                if leftDown() and rightDown():
                                    dads = scope * add * rxm * offset * offsetm2 * (C / 100) * smgoff
                            else:
                                dads = scope * add * rxm * offset * offsetm2 * (C / 100) * smgoff
                            dx = ((recoil[0] - lastShot[0]) / mult) * dads
                            dy = ((recoil[1] - lastShot[1]) / mult) * dads
                                    
                            s = time.time()
                            end = s + fr
                            moved = (0, 0)
                            while (time.time() < end):
                                t = (time.time() - s) / fr
                                b = max(min(t, 1.0), 0.0)
                                x = math.floor((dx * b) - moved[0])
                                y = math.floor((dy * b) - moved[1])

                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)

                                moved = tuple(map(operator.add, moved, (x, y)))
                                time.sleep(0.00001)

                            if cS == 'Semi':
                                if rightDown() and leftDown():
                                    break
    
                            dx = dx - moved[0]
                            dy = dy - moved[1]


                            lastShot = recoil

                            if wait > 0:

                                time.sleep(wait * boost)
                            if wep['mode'] == 'semi':
                                break
                            if leftDown() and rightDown():
                                continue
                            elif leftDown():
                                if not rightDown():
                                    if nonads == True:
                                        continue
                                    else:
                                        break
                            else:
                                lastShot = (0, 0)
                                n = 0
                                semicount = 0
                                if sa == False:
                                    shot = 1
                                break
                            
            else:
                lastShot = (0, 0)
                n = 0
                semicount = 0
                if sa == False:
                    shot = 1
    else:
        while True:
            main.update()
            if keyboard.is_pressed('r'):
                if sa == True:
                    shot = 1
                    n = 0
            if keyboard.is_pressed('shift + down arrow'):
                if C > 4:
                    C -= 5
                    lC.destroy()
                    lC = Label(main, text=f"Control: {C}%")
                    lC.place(x=10,y=40)
                    time.sleep(0.1)
                else:
                    C = 5
            if keyboard.is_pressed('shift + up arrow'):
                if C < 100:
                    C += 5
                    lC.destroy()
                    lC = Label(main, text=f"Control: {C}%")
                    lC.place(x=10,y=40)
                    time.sleep(0.05)
                else:
                    C = 100
            if keyboard.is_pressed('shift + m'):
                if rMode == 'Rage':
                    rMode = 'Legit'
                else:
                    rMode = 'Rage'
                rbl.destroy()
                rbl = Label(main, text=f"Recoil Mode: {rMode}")
                rbl.place(x=10,y=160)
                time.sleep(0.2)
            if keyboard.is_pressed('shift + left arrow'):
                if ran > 0:
                    ran -= 1
                    ral.destroy()
                    ral = Label(main, text=f"Randomization: {ran}")
                    ral.place(x=10,y=280)
                    time.sleep(0.1)
                else:
                    ran = 1
            if keyboard.is_pressed('shift + right arrow'):
                if ran < 10:
                    ran += 1
                    ral.destroy()
                    ral = Label(main, text=f"Randomization: {ran}")
                    ral.place(x=10,y=280)
                    time.sleep(0.1)
                else:
                    ran = 10
            if keyboard.is_pressed('shift + f6'):
                if active == False:
                    active = True
                    time.sleep(0.2)
                else:
                    active = False
                    time.sleep(0.2)
                awd.destroy()
                awd = Label(main, text=f"Active: {active}")
                awd.place(x=10,y=10)
            if antiafk == True:
                keyboard.press(AAK)
                keyboard.release(AAK)
                cd(30)
                if AAK == 'w':
                    AAK = 'a'
                elif AAK == 'a':
                    AAK = 's'
                elif AAK == 's':
                    AAK = 'd'
                elif AAK == 'd':
                    AAK = 'w'
            if ctrlDown():
                crouch = 0.5
            else:
                crouch = 1
            if keyboard.is_pressed('shift + v'):
                if nonads == True:
                    nonads = False
                else:
                    nonads = True
                hip.destroy()
                hip = Label(main, text=f"Hip Control: {nonads}")
                hip.place(x=10,y=310)
                time.sleep(0.2)
            if keyboard.is_pressed('shift + j'):
                scope = 1
                cS = 'Iron'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if keyboard.is_pressed('shift + ]'):
                scope = 3.83721
                cS = '8x'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if keyboard.is_pressed('shift + l'):
                scope = 1.18605
                cS = 'Holosight'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if keyboard.is_pressed('shift + k'):
                scope = 0.8
                cS = 'Simple'
                scop.destroy()
                scop = Label(main, text=f"Sight: {cS}")
                scop.place(x=10,y=100)
            if keyboard.is_pressed('shift + n'):
                boost = 0.9
                add = 1
                cA = 'Muzzle Boost'
                atta.destroy()
                atta = Label(main, text=f"Attatchment: {cA}")
                atta.place(x=10,y=130)
            if keyboard.is_pressed('shift + u'):
                boost = 1
                add = 0.8
                cA = 'Silencer'
                atta.destroy()
                atta = Label(main, text=f"Attatchment: {cA}")
                atta.place(x=10,y=130)
            if keyboard.is_pressed('shift + h'):
                boost = 1
                add = 1
                cA = 'None'
                atta.destroy()
                atta = Label(main, text=f"Attatchment: {cA}")
                atta.place(x=10,y=130)
            if keyboard.is_pressed('shift + -'):
                wep = tables['weapons']['M2']
                wepon.destroy()
                cW = 'M249'
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if keyboard.is_pressed('shift + o'):
                wep = tables['weapons']['LR']
                cW = 'LR-300'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if keyboard.is_pressed('shift + p'):
                wep = tables['weapons']['MP5']
                cW = 'MP5A4'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if keyboard.is_pressed('shift + i'):
                wep = tables['weapons']['AR']
                cW = 'Assault Rifle'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if keyboard.is_pressed('shift + .'):
                wep = tables['weapons']['SAR']
                cW = 'Semi'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if keyboard.is_pressed('shift + \\'):
                wep = tables['weapons']['CU']
                cW = 'Custom SMG'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if keyboard.is_pressed('shift + ['):
                wep = tables['weapons']['TH']
                cW = 'Thompson'
                wepon.destroy()
                wepon = Label(main, text=f"Weapon: {cW}")
                wepon.place(x=10,y=70)
            if nonads == True:
                if leftDown():
                    if not rightDown():
                        for recoil in wep['pattern']:
                            fr = wep['firerate']
                            if rightDown():
                                nads = scope * add
                                
                            else:
                                
                                if wep == tables['weapons']['AR']:
                                    nads = 0.61
                                elif wep == tables['weapons']['LR']:
                                    nads = 0.63
                                elif wep == tables['weapons']['MP5']:
                                    nads = 0.63
                            
                            dx = ((recoil[0] - lastShot[0]) / mult) * nads
                            dy = ((recoil[1] - lastShot[1]) / mult) * nads
                                    
                            s = time.time()
                            end = s + fr
                            moved = (0, 0)
                            while (time.time() < end):
                                t = (time.time() - s) / fr
                                b = max(min(t, 1.0), 0.0)
                                x = math.floor((dx * b) - moved[0])
                                y = math.floor((dy * b) - moved[1])

                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)

                                moved = tuple(map(operator.add, moved, (x, y)))
                                time.sleep(1 / 1000)

                            dx = dx - moved[0]
                            dy = dy - moved[1]



                            lastShot = recoil
                            if leftDown():
                                continue
                            else:
                                lastShot = (0,0)
                                break
                else:
                    shot = 1
                    lastShot = (0, 0)
                    
            if leftDown() and rightDown():
                if active == True:
                    for recoil in wep['pattern']:
                        doingads = True
                        fr = wep['firerate']
                        if shot < (wep['mag'] + xyz):
                            shot += 1
                            if wep['cdif'] == True:
                                offset = crouch
                                if offset == 0.5:
                                    if wep == tables['weapons']['M2']:
                                        offsetm2 = 0.98
                                    if wep == tables['weapons']['M2']:
                                        offsetm2 = 1
                                else:
                                    offsetm2 = 0.95
                            else:
                                offset = 1
                                offsetm2 = 1
                            if ran == 0:
                                rxm = 1
                                rym = 1
                            else:
                                rxm = (random.randrange((100 - ran), (100 + ran)) / 100)
                                rym = (random.randrange((100 - ran), (100 + ran)) / 100)
                            if rMode == 'Rage':
                                if wep == tables['weapons']['AR'] or tables['weapons']['LR']:
                                    ct = (wep['ct'][n]) / 1000
                                    if ct > wep['firerate']:
                                        fr = wep['firerate']
                                        wait = 0
                                    else:
                                        wait = wep['firerate'] - ct
                                        fr = wep['firerate'] - wait

                                else:
                                    fr = wep['firerate']
                                    wait = 0
                            else:
                                fr = wep['firerate']
                                wait = 0

                            if rMode == 'Rage':
                                n += 1
                                if wep == tables['weapons']['AR']:
                                    if n > 10:
                                        fr = fr + 0.01
                                        wait = wait - 0.01
                                if wep == tables['weapons']['LR']:
                                    if n > 5:
                                        fr = 0.1
                                        wait = 0.015
                            if cW == 'Custom SMG':
                                if cS == 'Iron':
                                    smgoff = 0.8
                                else:
                                    smgoff = 1
                            elif cW == 'Thompson':
                                if cS == 'Iron':
                                    smgoff = 0.8
                                else:
                                    smgoff = 1
                            else:
                                smgoff = 1
                            if nonads == True:
                                if leftDown():
                                    dads = 0.61
                                if leftDown() and rightDown():
                                    dads = scope * add * rxm * offset * offsetm2 * (C / 100) * smgoff
                            else:
                                dads = scope * add * rxm * offset * offsetm2 * (C / 100) * smgoff
                            dx = ((recoil[0] - lastShot[0]) / mult) * dads
                            dy = ((recoil[1] - lastShot[1]) / mult) * dads
                                    
                            s = time.time()
                            end = s + fr
                            moved = (0, 0)
                            while (time.time() < end):
                                t = (time.time() - s) / fr
                                b = max(min(t, 1.0), 0.0)
                                x = math.floor((dx * b) - moved[0])
                                y = math.floor((dy * b) - moved[1])

                                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)

                                moved = tuple(map(operator.add, moved, (x, y)))
                                time.sleep(1 / 1000)

                            dx = dx - moved[0]
                            dy = dy - moved[1]


                            lastShot = recoil

                            if wait > 0:

                                time.sleep(wait * boost)
                            if wep['mode'] == 'semi':
                                break
                            if leftDown() and rightDown():
                                continue
                            elif leftDown():
                                continue
                            else:
                                lastShot = (0, 0)
                                n = 0
                                if sa == False:
                                    shot = 1
                                break
                            
            else:
                lastShot = (0, 0)
                n = 0
                if sa == False:
                    shot = 1

