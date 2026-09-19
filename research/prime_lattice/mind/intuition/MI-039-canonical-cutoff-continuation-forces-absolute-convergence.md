# MI-039 — Canonical positive approximation plus ordinary evaluation cannot realize zeta continuation

**Evidence level:** exact synthesis from [PL-360](../../findings/PL-360-diagonal-weighted-hilbert-spaces-cannot-carry-zeta-continuation.md) through [PL-363](../../findings/PL-363-finite-signed-lattice-shift-filter.md).

PL-360 shows that no positive diagonal coefficient Hilbert metric can simultaneously contain the zeta coefficient vector and keep ordinary point evaluation bounded in the critical strip. PL-361 removes the diagonal and Hilbert assumptions from the most canonical completion repair.

Let `X` be any Hausdorff topological vector space of functions on a domain containing `s_0`. If the ordinary zeta partial sums

`Z_N(s)=sum_(n<=N) n^-s`

converge in `X` and point evaluation at `s_0` is continuous, continuity forces `Z_N(s_0)` to converge as scalars. The ordinary coefficient-one Dirichlet series converges only for `Re(s_0)>1`. Thus no completion can make the **canonical coefficient cutoffs themselves** converge while retaining ordinary continuous evaluation inside `Re(s)<=1`. The same obstruction applies when the Dirichlet monomials form a Schauder basis and the completed zeta vector has coefficient sequence `(1,1,...)`.

PL-362 closes the most obvious smoothing escape. Let `w_i(n)>=0` be any directed coefficientwise approximate identity with `w_i(n)->1` for every fixed `n`. At every real `sigma<=1`,

`F_i(sigma)=sum_n w_i(n)n^-sigma -> +infinity`.

No monotonicity, common finite support, Hilbert structure or continuity assumption is needed. Positivity plus coefficientwise recovery alone preserves the divergent mass. Positive Riesz-, Cesàro-, heat- or energy-style coefficient filters therefore cannot continue the coefficient-one zeta series across its real convergence wall by unrenormalized evaluation.

PL-363 gives the complementary signed control. For a fixed finite lattice-shift filter

`T=sum_(m in F) c_m S_m`,

the coefficient-one vector becomes the periodic sequence

`b_k=sum_(m|k)c_m`,

and on `Re s>1` its Dirichlet series is

`B(s)=P(s)zeta(s)`, with `P(s)=sum_m c_m m^-s`.

The period mean is `P(1)`. If `P(1)=0`, the coefficients have zero mean, the ordinary Dirichlet series converges locally uniformly on `Re s>0`, and this half-plane is sharp for ordinary convergence. Classical Hurwitz-zeta continuation then extends the periodic series after the pole cancellation. Thus **finite sign-indefinite cancellation is enough to cross the positive wall, but not enough to create a new zero selector**.

The one-prime filter `1-pS_p` makes the point especially clean: it produces the eta-type factor `(1-p^(1-s))zeta(s)`. For `p=2` the extra factor has its zeros on `Re s=1`, so it does not alter the zeta divisor in the critical strip. A general finite Dirichlet polynomial `P` can add its own zeros, but nothing in the finite shift construction forces those zeros to encode the critical line. The continuation gain comes from periodic pole cancellation, not from new rational-prime rigidity.

PL-363 therefore sharpens the lesson from PL-361--PL-362. Leaving the positive cone is a genuine mechanism change and can enlarge the ordinary convergence domain, but the sign pattern itself must still be **source-forced and destination-selective**. A chosen finite cancellation that merely turns the coefficient-one series into a classical periodic Dirichlet series has solved continuation without solving zero selection.

The reusable lesson is that **completion topology, approximation protocol, sign structure and continuation mechanism are one coupled interface**. Before crediting a new completion, state which approximants converge, where cancellation enters, whether it is forced by the arithmetic source or chosen externally, what renormalization is subtracted, in what topology convergence occurs, and which destination readout remains selective after continuation.

**Boundary.** PL-360--PL-363 do not prohibit analytic continuation, infinite or scale-dependent signed/complex summability, renormalized finite parts, non-diagonal mixing, rigged/distributional pairings, unbounded evaluation or source-forced global correlations. PL-363 classifies only fixed finite lattice-shift filters. It shows that the first obvious signed escape is classical periodic continuation, not that every sign-indefinite or renormalized continuation must be classical or zero-blind.