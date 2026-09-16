# MI-031 — Strong additive coupling collapses to the lowest output mode

**Evidence level:** exact synthesis from [PC-319](../../findings/PC-319-small-mordell-tornheim-coupling-preserves-off-critical-zeros.md), [PC-320](../../findings/PC-320-canonical-mordell-tornheim-off-critical-zeros-form-local-hypersurface.md), and [PC-321](../../findings/PC-321-large-mordell-tornheim-exponent-is-zero-free-on-right-polyhalfplane.md).

For the canonical `(5,7)` Mordell--Tornheim packet

`Z_(5,7)(s,t,u) = sum_(k,l>=1) a_5(k)b_7(l) / (k^s l^t (k+l)^u)`,

the two obvious coupling endpoints fail in opposite ways.

Near `u=0`, PC-319--PC-320 show that an off-critical zero of the decoupled one-level factor persists under genuine positive coupling and expands into a local analytic zero hypersurface over an open parameter set. Canonical source coefficients and multivariable nonseparability therefore do not clean the divisor near decoupling.

At large `Re u`, PC-321 proves a different exact phenomenon. The additive output frequency has a **unique minimum** at `(k,l)=(1,1)`. After multiplying by `2^u`, every other pair is bounded by the tail

`E(v)=sum_(n>=3) (n-1)(2/n)^v`,

which decreases to zero. For bounded source coefficients with `a(1)b(1)!=0`, sufficiently large `Re u` therefore forces first-mode domination and a zero-free right polyhalf-plane. In the canonical `(5,7)` case the explicit coefficient has modulus `cos(2pi/7)>1/2`, while `E(5)<1/2`, giving

`Z_(5,7)(s,t,u) != 0` for `Re s>=0`, `Re t>=0`, `Re u>=5`.

The conceptual boundary is that stronger nonlinear coupling need not create stronger zero selection. Here increasing the additive exponent eventually **removes** all competition among output modes and collapses the packet to one nonzero coefficient. The parameter `u` therefore interpolates between two bad regimes: weak coupling retains the off-critical source divisor, while strong coupling suppresses the divisor entirely.

Any RH-facing use of this canonical packet must consequently locate a source-forced mechanism at finite intermediate coupling. It is not enough to choose an arbitrary `0<u<5`; one needs an independent reason that a distinguished locus is selected and a theorem showing that its zero geometry excludes the known off-critical branch. A determinant or quotient could also change the zero set, but then its new divisor has to be analyzed on its own rather than inherited rhetorically from the raw packet.

The first-mode argument is reusable beyond `(5,7)`: whenever the additive output has a unique smallest frequency with nonzero source coefficient and the remaining coefficients are uniformly bounded, large positive additive exponent produces a zero-free region by elementary dominance. This is a structural warning for nonlinear Mellin couplings with ordered output frequencies.

**Boundary.** PC-321 says nothing about the finite strip `0<Re u<5`, does not exclude special intermediate submanifolds, and does not rule out different nonlinear couplings. The threshold `5` is an explicit sufficient value for the canonical pair, not a claimed optimal transition. The note is a zero-geometry boundary, not an RH implication.
