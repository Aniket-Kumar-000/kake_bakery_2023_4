@aetest.test        
    def powering_off_the_module_and_verifying_CC(self,testbed,testscript):
        global mod
        mod = testbed.custom['module']
        
        log.info(banner(f"-POWER DOWN- in the module {mod}"))
        uut1.configure(r"""poweroff module %s"""%(mod))    
        time.sleep(10)
        ouT = uut1.execute(r"""show mod""")
        if 'powered-dn' in ouT:
            log.info(f"PASSED , successfully -POWER DOWN- in module {mod}")
        else:
            log.info(f"FAILURE , -POWER DOWN- is not showing for module {mod}")
            self.failed()
        
        log.info(banner(f"Verifying the CC in -POWER DOWN- condition of module {mod}"))
        O = buglib.cc_check(uut1)
        if 'failed' in O:
            log.info(f"FAIL: CC is getting Failure for module {mod} when -POWER DOWN-")
            self.failed()
        else:
            log.info(f"CC passed when -POWER DOWN- in module {mod}")
            
    @aetest.test
    def unconfiguring_and_powering_on(self,testbed,testscript):
        global mod
        mod = testbed.custom['module']
        log.info(banner(f"-POWER ON- to the module {mod}"))
        uut1.configure(r"""no poweroff module %s"""%(mod))
        log.info("Please Wait for 5 minutes...")
        time.sleep(350)
        OuT = uut1.execute("""show mod""")
        if 'powered-dn' in OuT:
            log.info(f"FAILED: module {mod} not showing 'ok' after -POWER ON-")
            self.failed()
        else:
            log.info(f"PASSED: module {mod} came up after -POWER ON-")
          
        # make changes in below line   
        log.info(banner(f"Removing every configurations from ports {uut1_1_intf1} , {uut1_1_intf2} , {uut1_2_intf1} , {uut1_2_intf2} , {uut1_3_intf1} , {uut1_3_intf2}"))    
        # till here
        down = "no"
        for i in interface:
             buglib.storm(i,down,uut1)   
