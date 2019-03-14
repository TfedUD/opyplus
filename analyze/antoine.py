import os

import oplus as op

if __name__ == "__main__":
    epm = op.Epm(os.path.join(
        op.CONF.eplus_base_dir_path,
        "ExampleFiles",
        "1ZoneEvapCooler.idf")
    )
    # epm = op.Epm()

    # print([epm])
    # print(epm)
    # print(epm.get_info())

    # bsd_table = epm.BuildingSurface_Detailed
    # print([bsd_table])
    # print(bsd_table)
    # print(bsd_table.get_info())

    # bsd = bsd_table.select()[0]
    # print([bsd])
    # print(bsd)
    # print(bsd.get_info())


    # zone = epm.Zone.add(name="Test")
    print(epm.to_idf())

    epm.set_defaults()
    print(epm.to_idf())
    # print(zone._data)

    #
    # #print(zone.get_info())
    #
    # sch = epm.Schedule_Compact.add(name="sch")
    # #print(sch.get_info())
    #
    # zl = epm.ZoneList.add(name="zl")
    # #print(zl)
    # #print(zl.get_info())
    #
    # eq = epm.ZoneHVAC_EquipmentList.add(name="eq")
    # eq2 = epm.ZoneHVAC_EquipmentList.add(name="eq")
    # print(eq.get_info())

