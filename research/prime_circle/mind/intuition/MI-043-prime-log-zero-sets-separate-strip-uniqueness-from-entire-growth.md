# MI-043 — Prime-log zero sets separate strip uniqueness from entire growth

**Evidence level:** exact synthesis from [PC-341](../../findings/PC-341-prime-log-uniqueness-extends-to-bounded-characteristic-on-gamma-strip.md) and [PC-342](../../findings/PC-342-prime-log-entire-survivors-require-infinite-order.md). The Blaschke, Jensen and Weierstrass mechanisms are classical; the Mathia content is their placement at the Prime-Circle semiprime interpolation boundary.

PC-341 identified a sharp strip-domain threshold: on the native Gamma strip of half-width `pi/2`, the prime logarithms are a uniqueness set for bounded-characteristic functions, while on every narrower strip a nonzero bounded Blaschke survivor can vanish on all prime logs.

PC-342 shows that passing from strip control to full-plane analyticity does not by itself restore uniqueness. If an entire function vanishes at all but finitely many prime logarithms, its zero counting function grows like `pi(e^r)~e^r/r`; this is incompatible with every finite order. Hence any nonzero entire survivor must have infinite order. Conversely, canonical Weierstrass products with those zeros exist, and symmetry/reality/nonnegativity can be imposed without removing the escape.

The admissibility boundary is therefore two-dimensional. **Domain extension and growth control are independent resources.** Full-plane analyticity is stronger in domain but weaker than the native-strip Nevanlinna hypothesis in growth; it admits infinite-order prime-log zero carriers that bounded characteristic forbids. Finite-order entire, Cartwright and exponential-type repairs are ruled out, but arbitrary entire continuation is not.

For a scalar Mellin selector, saying that the interpolation function is entire is therefore not a closure theorem. One must state a growth class strong enough to make the prime-log set coercive, or add source constraints beyond the zero set. Leaving bounded characteristic merely to gain analytic continuation exchanges one kind of control for another.

**Boundary.** PC-342 constructs admissible zero-set carriers, not Prime-Circle shell selectors satisfying all semiprime relations, and it supplies no Riemann-zero destination theorem. Infinite order is a necessary cost for the entire zero-set escape, not evidence that such an escape is useful.