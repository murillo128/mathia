# MI-030 — Canonical Mordell--Tornheim coupling carries an off-critical local divisor near decoupling

**Evidence level:** proved for the smallest canonical Prime-Circle pair by [PC-319](../../findings/PC-319-small-mordell-tornheim-coupling-preserves-off-critical-zeros.md) and strengthened by [PC-320](../../findings/PC-320-canonical-mordell-tornheim-off-critical-zeros-form-local-hypersurface.md), using the classical Saias--Weingartner zero theorem, Rouché stability and Weierstrass preparation.

The genuinely two-index carrier of PC-316 is not rescued merely by using the exact Prime-Circle coefficient vector. For the canonical `(q,r)=(5,7)` source, the one-level factor `A_5(s)` lies outside the exceptional `P(s)L(s,chi)` class and therefore has zeros in `Re s>1` inside absolute convergence.

At the decoupled face the exact identity is

`Z_(5,7)(s,t,0)=A_5(s)B_7(t)`.

PC-319 fixed a real `T>1` with `B_7(T)!=0` and proved that the corresponding off-critical zero persists for every sufficiently small positive real coupling `u`. PC-320 shows that this was only a one-dimensional trace of a stronger local geometry. The Mordell--Tornheim series is jointly holomorphic in a full complex neighborhood crossing `u=0`; Weierstrass preparation in `s` therefore turns a zero `(s_0,T,0)` of multiplicity `m` into a degree-`m` local analytic hypersurface finite over an open bidisk of `(t,u)` parameters. After shrinking the neighborhood, every nearby parameter pair has at least one zero with `Re s>1`.

Thus the obstruction is not a bad frozen slice. **The canonical source-specific zero divisor itself contains an open-parameter off-critical component near decoupling.** Multiplication by a holomorphic nowhere-zero completion factor preserves that divisor exactly, while a local biholomorphic coordinate change preserves its dimension and only relabels it.

The surviving multivariable route must therefore add a selector not present in the raw divisor: a source-forced special locus separated from this neighborhood, a relation among several divisor components, a determinant or quotient with genuinely different zero geometry, or a different coupling. Standard gamma/exponential completion and coordinate mixing cannot provide the missing zero-selection theorem.

**Boundary.** The result is local near the decoupled face and does not rule out a distinguished positive-coupling locus bounded away from `u=0`, a different nonlinear source coupling, or a mixed-variable theorem built from more than one completed copy of the present packet. It does rule out treating the full nearby divisor, ordinary completion, or coordinate reparameterization as a Riemann-like selector by themselves.
