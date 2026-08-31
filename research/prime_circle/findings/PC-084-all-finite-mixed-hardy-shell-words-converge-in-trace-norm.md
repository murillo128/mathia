# PC-084 — all finite mixed Hardy shell words converge in trace norm under natural finite sections

**Status:** `EXACT-DERIVED` + `NOVELTY-CORRECTION` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-REDIRECTION`. The finite-section convergence theorem below is derived exactly from the Prime-Circle Hardy channels. Standard trace-ideal continuity and the surrounding multichannel Hankel localization theory are classical. No theorem-level historical novelty is claimed.

PC-083 proved that cyclically separated root-channel and shell words converge ordinarily under the natural Hardy finite sections, so Abel damping is not needed in that sector. It left a narrower apparent boundary: repeated-shell words can contain reciprocal primitive roots, so individual root-channel expansions lose the uniform Dirichlet bound used there and might seem to require genuine regularization.

At the level actually intrinsic to Prime Circle — the **completed primitive shell operators** — that boundary disappears for every finite word containing at least two distinct shell labels.

Let

\[
(\Gamma_n)_{jk}=-\frac{c_n(j+k+1)}{j+k+1},\qquad j,k\ge0,
\]

and let `P_N` be the orthogonal projection onto `span{e_0,...,e_N}`. If a finite shell word

\[
W=\Gamma_{n_1}\Gamma_{n_2}\cdots\Gamma_{n_k}
\]

is **nonconstant**, meaning that at least two of the labels `n_i` are different, then

\[
\boxed{
\left\|
P_N\Gamma_{n_1}P_N\Gamma_{n_2}P_N\cdots
P_N\Gamma_{n_k}P_N
-
\Gamma_{n_1}\Gamma_{n_2}\cdots\Gamma_{n_k}
\right\|_{\mathcal S_1}
\longrightarrow0.
}
\]

Consequently every finite mixed-shell trace is an ordinary finite-section limit:

\[
\boxed{
\operatorname{Tr}
\bigl(P_N\Gamma_{n_1}P_N\cdots P_N\Gamma_{n_k}P_N\bigr)
\longrightarrow
\operatorname{Tr}
\bigl(\Gamma_{n_1}\cdots\Gamma_{n_k}\bigr).
}
\]

The result includes repeated-shell words such as `Gamma_3 Gamma_2 Gamma_3`. Thus PC-083's remaining finite-trace regularization warning must be narrowed: reciprocal **root channels** can still defeat termwise/rectangular root-channel summation, but once the complete primitive shells are assembled, every finite genuinely mixed shell word has a canonical ordinary finite-section trace. The core cyclically separated root theorem of PC-083 remains unchanged.

## 1. Root-channel setup

For a unit root `alpha`, recall from PC-075/PC-080

\[
(\mathcal H_\alpha)_{jk}
=\frac{\alpha^{j+k+1}}{j+k+1},
\qquad
\mathcal H_\alpha
=\alpha D_\alpha H D_\alpha,
\]

where

\[
D_\alpha e_j=\alpha^j e_j,
\qquad
H_{jk}=\frac1{j+k+1}.
\]

The primitive shell is the finite sum

\[
\boxed{
\Gamma_n=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha.
}
\]

PC-080 proved that if `alpha` and `beta` have different exact orders, then

\[
\gamma:=\alpha\beta\neq1
\]

and

\[
\mathcal H_\alpha\mathcal H_\beta\in\mathcal S_1.
\]

For the present finite-section theorem, trace-classness of the limiting product is not enough by itself: one must also control the extra high-mode excursion inserted between the two compressed factors.

## 2. A separated root pair converges in trace norm

Fix roots `alpha,beta` with

\[
\gamma=\alpha\beta\neq1.
\]

Write

\[
A=\mathcal H_\alpha,
\qquad
B=\mathcal H_\beta,
\qquad
P=P_N,
\qquad
Q=I-P.
\]

There is the exact decomposition

\[
\boxed{
PAPBP-AB
=
(PABP-AB)-PAQBP.
}
\]

Because `AB` is trace class and `P_N -> I` strongly,

\[
\boxed{
\|P_NABP_N-AB\|_1\longrightarrow0.
}
\]

This is the standard trace-ideal finite-rank approximation fact: for a fixed `T in S_1`, both `(I-P_N)T` and `T(I-P_N)` tend to zero in trace norm. It follows directly by first checking finite-rank `T` and then approximating an arbitrary trace-class operator in `S_1`.

The only new term is therefore the cross-tail `PAQBP`.

## 3. The cross-tail has an explicit Dirichlet estimate

Since `P,Q` commute with every diagonal `D_alpha`,

\[
PAQBP
=
\alpha\beta\,
D_\alpha
\bigl(PH QD_\gamma HP\bigr)
D_\beta.
\]

The outer diagonal factors are unitary, so the trace norm is exactly the trace norm of

\[
E_N:=PH QD_\gamma HP.
\]

On the finite range of `P_N`, its matrix entries are

\[
\boxed{
(E_N)_{jk}
=
\sum_{r>N}
\frac{\gamma^r}
{(j+r+1)(k+r+1)},
\qquad 0\le j,k\le N.
}
\]

Because `gamma != 1`, every finite partial sum of its powers satisfies

\[
\left|\sum_{r=a}^{b}\gamma^r\right|
\le
C_\gamma,
\qquad
C_\gamma:=\frac2{|1-\gamma|}.
\]

For fixed `j,k`, the positive sequence

\[
a_r=\frac1{(j+r+1)(k+r+1)}
\]

is decreasing to zero. Dirichlet summation by parts therefore gives the uniform tail bound

\[
\boxed{
|(E_N)_{jk}|
\le
\frac{C_\gamma}
{(N+j+2)(N+k+2)}.
}
\]

Hence

\[
\begin{aligned}
\|E_N\|_2^2
&\le
C_\gamma^2
\left(
\sum_{j=0}^N\frac1{(N+j+2)^2}
\right)^2\\
&\le
C_\gamma^2
\left(\frac{N+1}{(N+2)^2}\right)^2.
\end{aligned}
\]

Thus

\[
\boxed{
\|E_N\|_2=O_\gamma(N^{-1}).
}
\]

Since `E_N` has rank at most `N+1`, the Schatten inequality

\[
\|E_N\|_1
\le
\sqrt{N+1}\,\|E_N\|_2
\]

gives the stronger estimate needed here:

\[
\boxed{
\|E_N\|_1
\le
C_\gamma\frac{(N+1)^{3/2}}{(N+2)^2}
=O_\gamma(N^{-1/2})
\longrightarrow0.
}
\]

Combining the two pieces proves

\[
\boxed{
\left\|
P_N\mathcal H_\alpha P_N\mathcal H_\beta P_N
-
\mathcal H_\alpha\mathcal H_\beta
\right\|_1
\longrightarrow0
\qquad(\alpha\beta\neq1).
}
\]

This is exactly the estimate missing from a naive appeal to `AB in S_1`: the finite sections permit an excursion through modes above `N`, and cyclotomic oscillation forces that excursion to vanish in trace norm.

## 4. Distinct completed shells inherit the convergence

Let `m != n`. For every

\[
\alpha\in P_m^*,
\qquad
\beta\in P_n^*,
\]

we have `alpha beta != 1`, because reciprocal roots have the same exact order. Expanding the two completed shells gives only finitely many separated root pairs. Therefore the root-pair estimate sums directly to

\[
\boxed{
\left\|
P_N\Gamma_mP_N\Gamma_nP_N
-
\Gamma_m\Gamma_n
\right\|_1
\longrightarrow0
\qquad(m\neq n).
}
\]

PC-080 had already proved `Gamma_m Gamma_n in S_1` and identified its trace with minus the logarithm of the cyclotomic resultant. The present statement is stronger in a different direction: it proves that the **intrinsic finite Hardy truncations themselves** converge to that trace-class operator, without radial damping or a summation prescription.

## 5. One distinct adjacent pair regularizes every finite mixed word

Consider a finite shell word

\[
(n_1,\ldots,n_k)
\]

that is not constant. Then some ordinary adjacent pair satisfies

\[
n_i\neq n_{i+1}.
\]

Define the trace-class core

\[
T_N
=P_N\Gamma_{n_i}P_N\Gamma_{n_{i+1}}P_N,
\qquad
T=\Gamma_{n_i}\Gamma_{n_{i+1}}.
\]

Section 4 gives

\[
\boxed{\|T_N-T\|_1\to0.}
\]

Write the remaining finite factors to the left and right as `L_N` and `R_N`, so that the full compressed word is

\[
W_N=L_NT_NR_N.
\]

Each `Gamma_n` is bounded, `P_N -> I` strongly, and there are only finitely many factors. Hence

\[
L_N\to L,
\qquad
R_N\to R
\]

strongly, the adjoints converge strongly as well, and the two sequences are uniformly bounded.

For completeness, the standard ideal-continuity step is elementary. If `X_N -> X` and `Y_N -> Y` strong-* with uniformly bounded norms and `S_N -> S` in `S_1`, then

\[
X_NS_NY_N\to XSY
\quad\text{in }S_1.
\]

Indeed, split the difference into

\[
X_N(S_N-S)Y_N
+(X_N-X)SY_N
+XS(Y_N-Y).
\]

The first term is controlled by the ideal norm. For the other two, approximate the fixed `S in S_1` by finite-rank operators; strong convergence is uniform on each resulting finite-dimensional range, and strong convergence of the adjoints handles right multiplication.

Applying this lemma gives

\[
\boxed{
\|W_N-W\|_1\longrightarrow0,
\qquad
W=\Gamma_{n_1}\cdots\Gamma_{n_k}.
}
\]

Thus a **single distinct adjacent shell pair is enough to create a trace-class core, and the natural finite sections preserve it through arbitrarily many bounded repeated-shell factors on either side.**

## 6. The repeated-shell control from PC-082 is ordinary, not regularized

PC-082 supplied the exact control

\[
\operatorname{Tr}(\Gamma_2\Gamma_3)=0
\]

but

\[
\boxed{
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0.
}
\]

The word `(3,2,3)` is deliberately outside the root-wise cyclic-separation theorem of PC-083: when the trace is expanded root by root, the wrap-around same-shell pair can contain reciprocal primitive roots.

Nevertheless it contains the distinct adjacent pair `(3,2)`. The theorem above therefore gives

\[
\boxed{
\operatorname{Tr}
\bigl(P_N\Gamma_3P_N\Gamma_2P_N\Gamma_3P_N\bigr)
\longrightarrow
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0.
}
\]

So the higher invariant that proves the Hardy shell algebra is richer than pairwise resultants is already selected by the most elementary intrinsic cutoff: keep the first `N+1` Hardy modes and let `N -> infinity`.

No Abel parameter is needed for its existence.

## 7. Why reciprocal root channels can still look singular

The shell-level theorem must not be misread as a termwise theorem for arbitrary primitive-root expansions.

If two adjacent root channels satisfy

\[
\beta=\alpha^{-1},
\]

then `gamma=alpha beta=1`. The Dirichlet bound in Section 3 disappears, and the cross-tail is built from the untwisted Hilbert singularity. An individual root-channel multiple series may therefore fail the rectangular-convergence argument of PC-083 or require a specified summation order.

What the present theorem shows is more structural:

\[
\boxed{
\text{root-wise reciprocal singularity}
\not\Rightarrow
\text{shell-wise regularization ambiguity}.
}
\]

When the word contains at least two distinct completed shells, it can be grouped around one distinct adjacent pair **before** expanding the other shells into primitive roots. That pair is trace class and its finite-section error tends to zero in `S_1`; the remaining repeated-shell operators are only bounded multipliers of this nuclear core.

Accordingly, arbitrary reorderings of a conditionally convergent root-channel or cone expansion are still unjustified. The canonical object is the completed shell operator word and its Hardy finite-section ordering.

## 8. Boundary: pure same-shell words are not repaired

The theorem requires a nonconstant shell word. If every label equals the same `n`, there is no distinct adjacent pair from which to obtain a trace-class core.

This is not merely a proof artifact. PC-080 already shows that the same-shell square is outside the trace class:

\[
\boxed{\Gamma_n^2\notin\mathcal S_1.}
\]

The reciprocal primitive channels are exactly where the smooth separated-kernel argument fails. Thus the present result does **not** assign traces to pure same-shell words and does not manufacture a renormalized trace for the Hilbert singular sector.

The corrected finite-order boundary is therefore

\[
\boxed{
\begin{array}{ll}
\text{finite nonconstant completed-shell words}
&\to \text{ordinary }\mathcal S_1\text{ finite-section convergence},\\[3pt]
\text{individual reciprocal root-channel expansions}
&\to \text{ordering/summability may still matter},\\[3pt]
\text{pure same-shell words}
&\to \text{no mixed trace-class core supplied here}.
\end{array}
}
\]

## 9. Prior-art and novelty audit

The operator-theoretic ingredients surrounding the result are classical.

1. Trace class is a two-sided ideal, finite-rank operators are dense in `S_1`, and uniformly bounded strong-* convergence acts continuously on a fixed trace-class operator. These are standard trace-ideal facts, not new Prime-Circle structure.
2. PC-080 already anchored the relevant multichannel Hankel prior art through Pushnitski--Yafaev: separated singular channels are expected to decouple modulo compact/trace-class effects. The new estimate is a concrete finite-section realization of that separation for the cyclotomic Hilbert channels.
3. The `O_gamma(N^{-1/2})` trace-norm estimate is an elementary consequence of bounded geometric partial sums plus the Hilbert--Schmidt-to-trace-norm rank bound. Directed searches for finite-section convergence of oscillatory Hilbert matrices, root-of-unity Hankel products, and cyclotomic Hankel traces found the standard trace-ideal/multichannel neighborhoods but no authoritative source stating this exact completed-shell specialization. Absence of that specialization is **not** treated as evidence of historical novelty.
4. PC-083's root-wise ordinary convergence under full cyclic separation remains valid and stronger at the level of individual channels. The present result addresses a different mechanism: cancellation/ideal structure after complete primitive shells have been assembled.

The durable contribution is therefore an internal classification and novelty correction: **finite mixed-shell higher traces are genuine Hardy operator invariants, but their existence does not rely on a special Abel regularization.**

## 10. RH relevance: finite-order regularization is not an analytic-parameter source

This closes a natural attempt to extract extra RH structure from the boundary singularity of repeated-shell higher traces.

At every finite mixed trace order, the canonical Hardy cutoff already converges in trace norm. There is therefore no regulator parameter whose removal could intrinsically generate a new complex spectral variable, functional equation, gamma factor, or critical-line symmetry. The higher traces of PC-082 can still contain strictly more arithmetic information than pairwise resultants, but that extra information is **ordinary finite-order relative operator data**, not a renormalization anomaly.

This does not classicalize the values themselves. In particular, PC-083's question of reducing cyclically separated cone periods to established cyclotomic multiple-polylogarithm values remains meaningful, and repeated-shell completed traces may still have richer arithmetic identities than the pairwise resultant graph.

Nor does the result address an infinite-shell or genuinely cross-level limit in which the number of factors, conductor range, or operator itself varies. A future analytic parameter would have to arise from such additional intrinsic Prime-Circle structure rather than from the finite-section definition of a fixed mixed word.

## 11. Falsification surface

The theorem has six direct audit points.

1. The channel normalization must be `Gamma_n=-sum_{alpha in P_n^*} H_alpha` with `H_alpha=alpha D_alpha H D_alpha`.
2. For `gamma=alpha beta != 1`, the exact identity `PAPBP-AB=(PABP-AB)-PAQBP` must hold, and the cross-tail must reduce unitarily to `E_N=PHQD_gamma HP`.
3. Dirichlet summation must give
   \[
   |(E_N)_{jk}|\le C_\gamma/((N+j+2)(N+k+2)),
   \]
   implying `||E_N||_1=O_gamma(N^{-1/2})`.
4. For distinct shell orders every primitive root pair must satisfy `alpha beta != 1`, allowing finite summation of the root-pair `S_1` convergence.
5. Every nonconstant finite linear word must contain an adjacent distinct pair, and the remaining compressed products must converge strong-* with uniform norm bounds, so the trace-class core propagates through the whole word.
6. The theorem must reproduce the PC-082 control
   \[
   \operatorname{Tr}(P_N\Gamma_3P_N\Gamma_2P_N\Gamma_3P_N)
   \to
   \operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0,
   \]
   while making no trace-class claim for the pure same-shell square `Gamma_n^2`.

Failure of points 1--5 invalidates the theorem. Point 6 checks both the claimed extension beyond PC-083's root-wise separated sector and the sharp same-shell boundary.

## Research consequence

The finite Hardy branch now has a cleaner hierarchy:

\[
\boxed{
\text{distinct pair}
\Rightarrow
\text{trace-class core}
\Rightarrow
\text{every finite mixed word has ordinary Hardy finite sections}.
}
\]

Therefore **finite-order summability is no longer an open escape route** for the Prime-Circle Hardy program. The meaningful remaining questions are about the arithmetic content of the resulting higher nuclear invariants, legitimate reduction to known cyclotomic period algebras, and genuinely infinite/cross-level constructions that derive rather than insert an analytic scale.