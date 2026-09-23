# MI-076 — Positive safe-line averages face a blind-or-singular defect dichotomy

**Evidence level:** supported by the exact one-defect boundary calculation [WI-424](../../findings/WI-424-kunik-boundary-flux-is-a-poisson-defect-counter.md), the fixed-line comparison [WI-425](../../findings/WI-425-fixed-safe-lines-are-cubically-blind-to-shallow-boundary-flux.md), and the multiscale obstruction [WI-426](../../findings/WI-426-kunik-multiscale-l2-has-blind-or-singular-dichotomy.md).

Kunik's boundary Blaschke flux gives an ideal positive defect observable. A defect of depth `d` contributes the Poisson profile

`2d/((t-gamma)^2+d^2)`,

whose `L^1` mass is constant and whose `L^2` energy is proportional to `1/d`. It therefore counts defects positively while becoming increasingly sensitive to shallow off-line displacement. The obstacle is that this boundary factor is itself defined from the unknown defects unless the source identity can recover it noncircularly.

WI-425 shows that moving to a fixed safe line loses exactly the sensitivity one would like to retain. For safe-line offset `a>d`, the corresponding one-defect logarithmic-derivative energy is

`2 pi d^2/[a(a^2-d^2)]`,

so at fixed `a` it is only quadratic in `d`, while the boundary energy is reciprocal in `d`. No finite family of fixed safe lines gives a uniformly bounded transfer back to the shallow-defect boundary scale.

WI-426 shows that a positive diagonal multiscale average does not repair this continuously. If the averaging measure stays safely away from the boundary and has finite inverse-cubic moment, the combined energy remains `O(d^2)` and is blind to shallow defects. If the required moment diverges, the observable is not finite; and if the averaging continuum reaches the defect depth, the kernel develops a nonintegrable resonance at `a=d` without an independent renormalization.

Thus the simplest positive route has a structural dichotomy: finite safe-line energy is too insensitive, while forcing enough near-boundary weight to imitate the reciprocal-depth counter makes the diagonal construction singular. A successful source-side bridge must therefore use additional structure—non-diagonal coupling, a justified renormalization, or a zeta-specific identity that transfers boundary information without averaging independent positive line energies.

**Boundary.** This is an exact obstruction for the stated one-defect kernels and positive diagonal multiscale class. It is not a no-go theorem for all Kunik/zeta couplings, interacting line observables, signed renormalized constructions, or source identities that correlate scales before taking energy.