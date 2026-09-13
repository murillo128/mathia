# MI-015 — Confluent volume is curvature-blind and controlled by radial depth

**Evidence level:** exact for the fixed-multiplicity finite-window Nyman volume by [NB-103](../../findings/NB-103-confluent-nyman-volume-is-curvature-blind-and-controlled-by-radial-depth.md), contrasted with the three-state conditioning law of NB-098--NB-102. No growing-multiplicity, repeated-zero or target-conversion theorem is claimed.

NB-102 shows that local three-state conditioning is geometric. After canonical deflation, the condition number is comparable to `(1+a/R)^4`, so high dimensionless Menger curvature can make a cluster arbitrarily ill-conditioned even when pairwise descriptions look harmless.

NB-103 proves that the corresponding fixed-multiplicity **normalized determinant volume** does not inherit this curvature singularity. The distinct-node determinant quotient has a removable, path-independent confluence limit: all collision Vandermonde factors cancel between numerator and denominator. After the large-cell limit, the coefficient depends only on

`x=2 Re(lambda_*) log q`

and multiplicity `d`, through

`Delta_d(x)=det[gamma(r+s+1,x)]_(r,s=0)^(d-1) / prod_(j=0)^(d-1)(j!)^2`.

Thus transverse, tangential and hierarchical collision paths with the same center and multiplicity have the same confluent volume coefficient even though NB-102 can assign them radically different condition numbers. Curvature is a **conditioning currency**, not a fixed-multiplicity determinant currency.

The volume resource is radial depth. `Delta_d(x)->1` exactly when the available depth tends to infinity, while near the boundary

`Delta_d(x)=c_d x^(d^2)(1+O_d(x))`.

So a fixed confluent packet loses normalized finite-window volume because `Re(lambda_*) log q` is too small, not because its local collision triangle has high curvature.

This separation changes the source-facing question. One must first identify what the downstream Nyman argument actually consumes. A stable inverse or coordinate reconstruction can require bounded Menger curvature. A fixed-cardinality determinant estimate instead requires enough radial depth. Treating a large condition number as automatic determinant-volume loss, or a good determinant as stable coordinates, is now invalid.

**Boundary.** The derivative estimates behind NB-103 are not uniform as `Re(lambda_*)->0` or `d->infinity`. Genuine repeated zeros require derivative/Jordan states rather than only distinct-node confluence, and growing packets may introduce new invariants. No statement is made about the actual distribution of zeta-zero clusters or about which currency the final Nyman target ultimately requires.
