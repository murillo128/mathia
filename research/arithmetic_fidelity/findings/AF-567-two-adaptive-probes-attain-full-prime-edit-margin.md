# AF-567 — Two adaptive probes attain the full prime-edit identification margin

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-EDIT · ADAPTIVE-IDENTIFICATION · DETERMINISTIC-SUP-NORM-NOISE · SHARP-TWO-QUERY-RESULT · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Theorem: adaptivity removes the finite-probe minimax loss

Retain precisely AF-562's experiment: a known finite set \(S=\{p_1<\cdots<p_m\}\) of at least two odd rational-prime **edit locations**, an unknown source \(\Phi_{p_i}:(0,\infty)\to\mathbb R\), and observations \(y=\Phi_{p_i}(a)+\eta\) with adversarial \(|\eta|\le\varepsilon\) at each chosen coordinate. The edited systems are generalized-prime matched controls, not alternative rational-prime systems. The common critical-coordinate calibration, full critical-index limit, and deterministic absolute-noise convention are unchanged.

Put
\[
G_i(a)=\Phi_{p_{i+1}}(a)-\Phi_{p_i}(a)>0,\qquad
D_i=\sup_{a>0}G_i(a),\qquad
d(S)=\min_{i<m}D_i=2\varepsilon_{\rm full}(S).
\tag{1}
\]
A deterministic adaptive two-query protocol chooses \(a_0\) before observing data and, after seeing \(y_0\), may choose \(a_1=a_1(y_0)\); it must uniquely identify the source for every source and every error sequence satisfying the announced bound \(\varepsilon\). Let \(\varepsilon^{\rm ad}_2(S)\) be the supremum of admissible \(\varepsilon\) over such protocols (equality at the supremum need not allow unique decoding).

**Exact eventual saturation.** There exists \(P_0\) such that **every** finite \(S\) with \(\min S\ge P_0\), with unrestricted cardinality and logarithmic diameter, satisfies
\[
\boxed{\qquad
\varepsilon^{\rm ad}_2(S)
=\varepsilon_{\rm full}(S)=\tfrac12 d(S).
\qquad}
\tag{2}
\]
Indeed, AF-563 supplies a source-independent *first* coordinate, conditional only on the known set \(S\):
\[
a_0(S)=\frac{e^{-B_1}\,6\log(3/2)}{\log(1/d(S))}.
\tag{3}
\]
For every sufficiently large \(\min S\), **all** adjacent gaps at that coordinate satisfy
\[
\min_{i<m}G_i(a_0)\ge(\rho-o(1))d(S)>\tfrac12d(S),
\qquad
\rho=\frac{8e}{9}\log(3/2)=0.9797052759\ldots.
\tag{4}
\]
The \(o(1)\) is uniform over all finite candidate sets, as established in AF-563. This strict half-margin bound, not an exact peak approximation, is the entire arithmetic input for the adaptive conclusion.

## General finite ordered-profile locator lemma

Let \(F_1<\cdots<F_m\) be real-valued profiles with strict pointwise order on a common query domain. Assume
\[
d=\min_{i<m}\sup_a(F_{i+1}(a)-F_i(a))>0.
\]
If there is a coordinate \(a_0\) with
\[
\min_{i<m}[F_{i+1}(a_0)-F_i(a_0)]>\frac d2,
\tag{5}
\]
then the supremal worst-case unique-decoding radius of a deterministic adaptive protocol with at most two queries equals \(d/2\). For \(m=2\) the assertion is immediate even without (5).

**Proof (achievability).** Fix any \(0\le\varepsilon<d/2\). Make the first query at \(a_0\), obtaining \(y_0\), and form the exact interval-compatible version space
\[
V(y_0)=\{i:\ |y_0-F_i(a_0)|\le\varepsilon\}.
\tag{6}
\]
The true index belongs to \(V(y_0)\). If three indices \(i<j<k\) were compatible, pointwise order would imply that all indices between \(i\) and \(k\) are compatible and
\[
F_k(a_0)-F_i(a_0)\le2\varepsilon<d.
\]
But the span contains at least two adjacent gaps, each greater than \(d/2\), making the same span greater than \(d\), a contradiction. Thus \(V(y_0)\) contains either one index or exactly two **adjacent** indices.

A singleton is decoded immediately. In the two-index case, write \(V(y_0)=\{i,i+1\}\). Since
\[
\sup_a(F_{i+1}(a)-F_i(a))\ge d>2\varepsilon,
\]
choose a second coordinate \(a_1(y_0)\) at which that particular adjacent gap exceeds \(2\varepsilon\). The two possible \(\varepsilon\)-observation intervals are disjoint there, so the second observation decodes uniquely. This holds against arbitrary, mutually unrelated adversarial errors at the two coordinates.

**Proof (optimality).** Choose an adjacent pair with supremum distance exactly \(d\), which exists because the family is finite. For either member of that pair, an adversary allowed \(\varepsilon=d/2\) can return the **same** value \((F_i(a)+F_{i+1}(a))/2\) at every queried coordinate \(a\). The two data histories, and therefore every query location selected by a deterministic adaptive policy, are identical. No adaptive policy with any finite number of queries can distinguish the pair at that radius. Hence the supremal radius is at most \(d/2\), proving the lemma. \(\square\)

## Prime-edit consequence and strict nonadaptive separation

Insert \(F_i=\Phi_{p_i}\) into the lemma. AF-559 gives strict pointwise order and positive finite pair distances, AF-562 identifies the full-curve radius as \(d(S)/2\), and AF-563's explicit universal sample (3) satisfies (5) uniformly for all sufficiently large \(\min S\). This proves (2) with no new prime-gap input and without limiting \(|S|\).

The conclusion is **not** another estimate for the nonadaptive \(k\)-probe radius \(\varepsilon_k(S)\) in AF-562--AF-566: the second coordinate here is selected *after* seeing \(y_0\). In particular, AF-565's six-prime sequences satisfy
\[
\frac{\varepsilon_2(S_n)}{\varepsilon_{\rm full}(S_n)}
\longrightarrow
\vartheta_2=0.994878528675\ldots<1,
\qquad
\frac{\varepsilon^{\rm ad}_2(S_n)}{\varepsilon_{\rm full}(S_n)}
=1
\quad\text{eventually}.
\tag{7}
\]
Therefore adaptivity yields a **strict** worst-case separation for the *same two-query budget*, even with adversarial rather than stochastic error. AF-562/AF-563's four-prime examples also show that a single query is not universally sufficient to attain the full-curve margin; two queries are the smallest universally sufficient adaptive budget in the asymptotic prime-edit source class.

## Prior art, decisive checks, and limits

Sequential/response-adaptive experimental design and version-space reduction are classical ideas. Atkinson--Fedorov and Braess--Dette (bibliography under AF-562), and the adaptive-design literature represented by Foster--Ivanova--Malik--Rainforth (ICML 2021; bibliography under AF-567), establish the general setting but are **not** asserted to contain this ordered-profile, deterministic \(L^\infty\)-margin theorem. The ordered-profile locator lemma is elementary; no claim of broad methodological novelty is made. The source-specific mathematical increment is that AF-563's uniform, arbitrarily-large-family **one-sample** guarantee crosses exactly the threshold needed for *full-margin, two-query adaptive* decoding, while AF-565 supplies a strict nonadaptive comparison.

Falsification checks: the first posterior uses the actual announced \(\varepsilon\) rather than an unjustified zero-noise ranking; its index set is an interval only because all source curves are strictly ordered at the **same** coordinate; the \(\min G_i(a_0)>d/2\) condition is used to rule out **three** plausible sources and is not misread as one-query unique decoding; the selected second gap is \(>2\varepsilon\) for every \(\varepsilon<d/2\), even when its supremum equals \(d\); and a common midpoint adversarial transcript proves the full-curve upper bound for adaptive as well as nonadaptive policies. The result does not assume one common noise realization for the two queries.

The protocol requires the candidate set and a quantitative noise bound to be known to the experimenter, permits a data-dependent second query and arbitrarily accurate choice of the pair-specific coordinate, and retains the source-common critical calibration. It does not apply automatically to fixed prechosen samples, independently recalibrated coordinates, uncertain candidate families, stochastic/unbounded errors, or finite-index approximations. Crucially \(d(S)/2\) can still vanish arbitrarily fast; equal relative fidelity does **not** yield a fixed positive absolute stability modulus, an arithmetic-prime versus generalized-prime separator, or an RH consequence.

## Consequence for Arithmetic Fidelity

In this exact prime-edit family, **nonadaptive coverage of all plausible bottleneck scales** and **adaptive source identification** are different structural information budgets. Once one coarse observation rules out every triple of ordered alternatives, a targeted second observation restores the entire full-curve margin. The multi-probe loss constants of AF-564--AF-566 remain correct for their explicitly nonadaptive protocol, but they cannot be transferred unchanged to sequentially chosen observation coordinates.
