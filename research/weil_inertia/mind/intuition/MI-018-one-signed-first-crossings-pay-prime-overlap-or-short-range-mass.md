# MI-018 — One-signed first crossings must pay every cut with prime overlap or bilateral short-range mass

**Evidence level:** exact on the one-signed branch of a hypothetical first unrestricted Suzuki crossing through WI-270, using the classical Hilbert--Carleman inequality. No theorem makes the actual first null mode one-signed, forces a prime autocorrelation, or proves RH.

WI-269 gives the exact source-ground-state transform at a first crossing: multiplier energies form a positive-semidefinite signed-source Laplacian, while the archimedean source changes sign at `h_0=log rho`. WI-270 sharpens that structure when the null mode `v` is one-signed.

For almost every spatial cut `t`, firstness gives a positive lower energy cost to each half-mode. The exact cut energy can be written as prime-power crossing overlap plus archimedean crossing overlap. On the one-signed branch every crossing integrand is nonnegative, so the long-range archimedean part, where the source weight is negative, may be discarded in an upper bound. The remaining positive short-range kernel is dominated by `(2h)^(-1)`, and the sharp Hilbert--Carleman inequality gives the cut tariff

`P_t + (pi/2) sqrt(m_L(t)m_R(t)) >= max(lambda_(r_L(t)) M_L(t), lambda_(r_R(t)) M_R(t))`.

This creates a local alternative that is stronger than support domination. A cut must be paid either by positive prime-power overlap crossing that cut or by definite `L^2` mass within distance `h_0` on both sides. If every active prime autocorrelation is completely screened, one-signedness forces every prime crossing term to vanish pointwise, so the tariff becomes a quantitative bilateral concentration law. At a median cut it yields `m_L m_R >= (lambda_(a/2)/pi)^2`, and an internal essential-support gap of length at least `2h_0` is impossible.

The surviving question is therefore constructive rather than merely topological: can the family of screened cut tariffs propagate the forced short-range mass until some active prime-power translate must overlap, or can a genuine one-signed null geometry remain prime-screened while satisfying the Carleman concentration requirement at every cut? The first outcome would turn source-specific order into arithmetic overlap; the second would be a decisive source-compatible negative control.

**Boundary.** The sign assumption is load-bearing. For sign-changing modes the crossing integrand has no fixed sign and the long-range archimedean term cannot be dropped; WI-269's nodal compensation law remains the correct constraint. The constant `pi` is the generic Carleman norm, so improving it without extra Suzuki structure is not a free analytic refinement.