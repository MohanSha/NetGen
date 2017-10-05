import csv

htext="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
  <!--Created by yEd 3.17-->
  <key for="port" id="d0" yfiles.type="portgraphics"/>
  <key for="port" id="d1" yfiles.type="portgeometry"/>
  <key for="port" id="d2" yfiles.type="portuserdata"/>
  <key attr.name="Name" attr.type="string" for="node" id="d3"/>
  <key attr.name="url" attr.type="string" for="node" id="d4"/>
  <key attr.name="description" attr.type="string" for="node" id="d5"/>
  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="graphml" id="d7" yfiles.type="resources"/>
  <key attr.name="url" attr.type="string" for="edge" id="d8"/>
  <key attr.name="description" attr.type="string" for="edge" id="d9"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>
  <graph edgedefault="directed" id="G"> \n
"""
svgnodetext="""
        <node id="n%d">
        <data key="d3"><![CDATA[%s]]></data>
        <data key="d6">
            <y:SVGNode>
            <y:Geometry height="33.801994323730469" width="42.398406982421875" x="-118.29437408411025" y="594.7073565079138"/>
            <y:Fill color="#CCCCFF" transparent="false"/>
            <y:BorderStyle color="#000000" type="line" width="1.0"/>
            <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="33.40234375" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="72.02734375" x="-14.814468383789062" y="17.80199432373047">%s
                <y:LabelModel>
                <y:SmartNodeLabelModel distance="4.0"/>
                </y:LabelModel>
                <y:ModelParameter>
                <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="-0.5" nodeRatioX="0.0" nodeRatioY="0.5" offsetX="0.0" offsetY="4.0" upX="0.0" upY="-1.0"/>
                </y:ModelParameter>
            </y:NodeLabel>
            <y:SVGNodeProperties usingVisualBounds="true"/>
            <y:SVGModel svgBoundsPolicy="0">
                <y:SVGContent refid="%d"/>
            </y:SVGModel>
            </y:SVGNode>
        </data>
        </node>
        
        """
cloudnodetext="""
        <node id="n%d">
            <data key="d3"/>
            <data key="d6">
                <y:GenericNode configuration="com.yworks.flowchart.cloud">
                <y:Geometry height="179.4008908685969" width="179.1670378619154" x="87.51781737193764" y="139.14699331848564"/>
                <y:Fill hasColor="false" transparent="false"/>
                <y:BorderStyle color="#000000" type="line" width="1.0"/>
                <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="33.40234375" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="71.365234375" x="53.900901743457695" y="72.99927355929844">%s
                    <y:LabelModel>
                    <y:SmartNodeLabelModel distance="4.0"/>
                    </y:LabelModel>
                    <y:ModelParameter>
                    <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/>
                    </y:ModelParameter>
                </y:NodeLabel>
                </y:GenericNode>
            </data>
            </node>

            """
cloudconnectnodetext=""


fname=input("Enter file name to save: ")
fw= open("output\\"+fname+".graphml","a+")         
fw.write(htext)

nodelist=[]
typelist=[]
nid=0
with open('data/node.csv') as f:
    reader = csv.reader(f)
    for Node_name, Type in reader:
        nodelist.append(Node_name)
        typelist.append(Type)
        print(nodelist, typelist)
        print(len(nodelist))
    for i in range(0, len(nodelist)):
        print(i)
        print(nodelist[i])
        print("\nNode ID :",nid)
        label=nodelist[nid] 
        resid=typelist[nid]
        print(label, resid)
        if typelist[i]=="0":
            node=cloudnodetext
            print(node %(int(nid), label))
            fw.write(node %(int(nid), label))
        else:
            node=svgnodetext
            print(node %(int(nid), label, label, int(resid)))
            fw.write(node %(int(nid), label, label, int(resid)))
            pass
       
        
        nid+=1

eid=0
with open('data/edge.csv') as e:
    ereader = csv.reader(e)
    for Source, Target in ereader:
        print(Source, Target)
        
 
        edge="""
        <edge id="e%d" source="n%d" target="n%d">
        <data key="d10">
            <y:PolyLineEdge>
            <y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>
            <y:LineStyle color="#000000" type="line" width="1.0"/>
            <y:Arrows source="none" target="standard"/>
            <y:BendStyle smoothed="false"/>
            </y:PolyLineEdge>
        </data>
        </edge>
        """
        print(edge %(int(eid), int(Source), int(Target)))
        fw.write(edge %(int(eid), int(Source), int(Target)))
        eid+=1

file = open('foot.txt', 'r')
ftext = file.read()
fw.write(ftext)




file.close() #foot close
fw.close() #graphml close