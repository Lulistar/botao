# importando as bibliotecas da first

import wpilib
import wpilib.drive
import ctre 

# criando a classe

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):

# motor puxar

        self.m_puxar = ctre.WPI_VictorSPX(4)

# motor jogar

        self.m_jogar = ctre.WPI_VictorSPX(6)

# motor esteira

        self.m_esteira = ctre.WPI_VictorSPX(9)

# motor subir

        self.m_subir = ctre.WPI_VictorSPX(5)

# joystick

        self.controle = wpilib.Joystick(1)

# periodo teleop.

    def teleopInit(self):
        self.myRobot.setSafetyEnabled(True)

# Prog. 0 m_puxar

        if self.controle.getRawButton(0) == True:
            self.m_puxar.set(1)
        else:
            self.m_puxar.set(0)

# Prog. 1 m_jogar

        if self.controle.getRawButton(1) == True:
            self.m_jogar.set(1)
        else:
            self.m_jogar.set(0)
        
# Prog. 2 m_esteira

        if self.controle.getRawButton(2) == True:
            self.m_esteira.set(1)
        else:
            self.m_esteira.set(0)

# Prog. 3 m_subir

        if self.controle.getRawButton(3) == True:
            self.m_subir.set(1)
        else:
            self.m_subir.set(0)





