"""
Purpose:
    The default ArcGIS Python Toolbox template, although fully functional, is a little difficult to quickly implement.
    As a result, this template is available to hopefully streamline the process just slightly.
Licence:
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
# import modules
import arcpy

class BusinessLogic(object):
    """
    This is a dummy class, a placehodler for the code you write doing the real
    work processing your data. Write, debug and test this first so you know it
    is working. Then, once you have your working business logic, create the rest
    of your toolbox below.
    """
    # def method(self):
        # your incredible business logic


def parameter(displayName, name, datatype, defaultValue=None,
    parameterType="Required", direction="Input"):
    """
    The parameter implementation makes it a little difficult to quickly
    create parameters with defaults. This method prepopulates the parameterType
    and direction parameters and leaves the setting a default value for the
    newly created parameter as optional. The displayName, name and datatype are
    the only required inputs.
    """
    # create parameter with a few defaults
    param = arcpy.Parameter(
        displayName=displayName,
        name=name,
        datatype=datatype,
        parameterType=parameterType,
        direction=direction
    )

    # set new parameter to a default value
    param.value = defaultValue

    # return the complete parameter object
    return param


class Toolbox(object):
    def __init__(self):
        """
        Define the toolbox properties here. Do not change the name of this
        class. ArcGIS locates this class by name. It will not be able to find
        the toolbox and your toolbox will not work if you modify this.
        """
        self.label = 'Toolbox'
        self.alias = ''

        # List of tool classes associated with this toolbox
        self.tools = [Tool1]

class Tool1(object):
    """
    Add documentation here explaining your tool. The name of this class
    identifying the tool is referenced as a list item above, in the Toolbox's
    self.tools list.
    """
    def __init__(self):
        """
        Define the tool class attributes, including your tool parameters.
        """
        self.label = 'Tool'
        self.canRunInBackground = False
        
        # optional, place in a toolset container, http://joelmccune.com/toolsets-in-python-toolboxes/
        self.category = 'Tools to ...'
        

        self.parameters = [
            """
            Create your parameters here using the parameter function.
            Make sure you leave the enclosing brackets and separate your
            parameters using commas.
            """
            # parameter('exDisplayName', 'exName', 'GPString', 'exDefault'),
            # parameter('ex2DisplayName', 'ex2Name, 'DEFile')
        ]

    def getParameterInfo(self):
        """
        Return your parameter list defined in the __init__ method for the tool.
        If you want to set any additional proprieties, such as filters, for your
        parameters, do this here. Just reference them using their index in the
        parameter list
        """

        # self.param[0].filter.list = ['Option1', 'Option2', 'Option3']
        # self.param[1].filter.list = ['xml'] # only xml files for DEFile

        return self.parameters

    def isLicensed(self):
        """
        Set whether tool is licensed to execute and replace this text with a
        good explanation of what you are doing here.
        """
        return True

    def updateParameters(self, parameters):
        """
        Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed.
        """
        return

    def updateMessages(self, parameters):
        """
        Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation.
        """
        return

    def execute(self, parameters, messages):
        """
        Reference the business logic captured in your object defined
        separately in the module, preferably above.
        """
        # instance = businessLogic() # create object instance
        # instance.method() # call the method you want
        return
