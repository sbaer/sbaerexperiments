---
layout: bootstrap
title: bootstrap
permalink: /bs/
tags: developer rhinocommon
---

===== Sample: Add Brep Box =====

C#
=====
```csharp
public static Rhino.Commands.Result AddBrepBox(Rhino.RhinoDoc doc)
{
  Rhino.Geometry.Point3d pt0 = new Rhino.Geometry.Point3d(0, 0, 0);
  Rhino.Geometry.Point3d pt1 = new Rhino.Geometry.Point3d(10, 10, 10);
  Rhino.Geometry.BoundingBox box = new Rhino.Geometry.BoundingBox(pt0, pt1);
  Rhino.Geometry.Brep brep = box.ToBrep();
  Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
  if( doc.Objects.AddBrep(brep) != System.Guid.Empty )
  {
    rc = Rhino.Commands.Result.Success;
    doc.Views.Redraw();
  }
  return rc;
}
```

VB.NET
=====
```vbnet
Public Shared Function AddBrepBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
  Dim pt0 As New Rhino.Geometry.Point3d(0, 0, 0)
  Dim pt1 As New Rhino.Geometry.Point3d(10, 10, 10)
  Dim box As New Rhino.Geometry.BoundingBox(pt0, pt1)
  Dim brep As Rhino.Geometry.Brep = box.ToBrep()
  Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
  If doc.Objects.AddBrep(brep) <> System.Guid.Empty Then
    rc = Rhino.Commands.Result.Success
    doc.Views.Redraw()
  End If
  Return rc
End Function
```

Python
=====
```python
import Rhino
import scriptcontext
import System.Guid

def AddBrepBox():
    pt0 = Rhino.Geometry.Point3d(0, 0, 0)
    pt1 = Rhino.Geometry.Point3d(10, 10, 10)
    box = Rhino.Geometry.BoundingBox(pt0, pt1)
    brep = box.ToBrep()
    rc = Rhino.Commands.Result.Failure
    if( scriptcontext.doc.Objects.AddBrep(brep) != System.Guid.Empty ):
        rc = Rhino.Commands.Result.Success
        scriptcontext.doc.Views.Redraw()
    return rc

if( __name__ == "__main__" ):
    AddBrepBox()
```



$$
\begin{align*}
& \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
= \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
& (x_1, \ldots, x_n) \left( \begin{array}{ccc}
\phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
\vdots & \ddots & \vdots \\
\phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
\end{array} \right)
\left( \begin{array}{c}
y_1 \\
\vdots \\
y_n
\end{array} \right)
\end{align*}
$$