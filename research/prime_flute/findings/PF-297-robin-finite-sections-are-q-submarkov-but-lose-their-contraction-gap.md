# PF-297 — Robin finite sections are q-sub-Markov but lose their contraction gap

**Status:** `EXACT-DERIVED + WEIGHTED-L1-CONTRACTION + SUB-MARKOV-REPRESENTATION + DECISIVE-NEGATIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-276-robin-normalization-is-inverse-positive-and-cannot-zero-the-fixed-axis-threshold-moment|PF-276]] constructs, in each fixed-axis parity chain, a positive generalized weight `q_j>0` with `q_j asymp j+1` that is conserved by the complete Robin-normalized source column. The accepted local clue `CLUE-source-weighted-return-potential-controls-mixed-response` asks whether this weight can control repeated return/reassembly in the actual mixed response.

There is an exact answer for the **Robin-normalization factor itself**. Every finite Galerkin inverse is a strict contraction on the weighted coefficient space `ell^1(q)`, and after conjugation by `q` it is a column-substochastic positive matrix. But the contraction gap is entirely finite-section tail leakage: for every fixed seam parameter and every fixed source row, the lost `q`-mass tends to zero as the section grows. Consequently the weighted operator norms tend to `1`, while the complete infinite Robin inverse is exactly `q`-mass preserving on nonnegative inputs.

Thus repeated fixed-axis Robin normalization cannot amplify the PF-296 source moment, but it also cannot supply the uniform discount needed to bound a return resolvent by a geometric-series argument. Any successful source-weighted return proof must obtain its summability from the actual forcing/escape balance, the physical `P/H` split, mixed Schur reassembly, support loss, or another factor outside this conservative Robin normalization.

## Claim

Fix one parity sector and fixed `s,r>0`. Use the notation of PF-276:

\[
M=I+R,
\qquad R=\mathcal R^{0,\varepsilon}_{s,r},
\qquad q=(q_j)_{j\ge0},
\qquad q_j>0,
\tag{1}
\]

where `R>=0` as an operator, every distinct matrix entry satisfies `R_{jk}<0`, and the generalized weight obeys the absolutely convergent coordinate identity `Rq=0`. Let `P_N` project onto the first `N+1` parity coordinates and put

\[
M_N=P_NMP_N,
\qquad S_N=M_N^{-1},
\qquad q^{(N)}=P_Nq.
\tag{2}
\]

Then:

1. the finite-section defect is exactly the omitted-tail flux
   \[
   \boxed{
   d_N:=M_Nq^{(N)}-q^{(N)}
   =-P_NR(I-P_N)q>0
   }
   \tag{3}
   \]
   componentwise;
2. `S_N` is entrywise strictly positive and
   \[
   \boxed{
   S_Nq^{(N)}=q^{(N)}-e_N,
   \qquad e_N:=S_Nd_N>0;
   }
   \tag{4}
   \]
3. on the weighted space
   \[
   \|a\|_{1,q}:=\sum_{j=0}^Nq_j|a_j|,
   \tag{5}
   \]
   one has the strict finite-dimensional contraction
   \[
   \boxed{
   \|S_Na\|_{1,q}\le\rho_N\|a\|_{1,q},
   \qquad
   \rho_N:=\max_{0\le i\le N}\frac{(S_Nq^{(N)})_i}{q_i}<1;
   }
   \tag{6}
   \]
4. nevertheless, for every fixed source index `i`, as `N->infinity` through `N>=i`,
   \[
   \boxed{
   \sum_{j=0}^Nq_j(S_N)_{ji}\longrightarrow q_i,
   }
   \tag{7}
   \]
   and therefore
   \[
   \boxed{\rho_N\longrightarrow1.}
   \tag{8}
   \]
   In particular there is no `rho<1` that bounds the `ell^1(q)` norm of all Galerkin Robin inverses uniformly in depth, even for one fixed pair `(s,r)`;
5. the complete inverse `S=M^{-1}` extends from finitely supported sequences to a positive contraction on `ell^1(q)` satisfying
   \[
   \boxed{
   \sum_jq_j(Sa)_j=\sum_jq_ja_j
   \quad\text{for every }a\ge0,
   }
   \tag{9}
   \]
   and `||S||_{ell^1(q)->ell^1(q)}=1`;
6. with `Q=diag(q_j)`, the conjugated complete kernel
   \[
   \Pi=QSQ^{-1}
   \tag{10}
   \]
   is column-stochastic on `ell^1`, while `\Pi_N=Q_NS_NQ_N^{-1}` is strictly column-substochastic. Hence arbitrary finite compositions of complete fixed-axis Robin normalizations with varying canonical seam parameters are `ell^1(q)`-nonexpansive and preserve `q`-mass on nonnegative inputs, but no uniform geometric return discount follows from the Robin factors alone.

## 1. The finite-section loss is exactly coupling to the omitted tail

PF-276 proves the absolutely convergent generalized harmonic identity `Rq=0` and, more quantitatively,

\[
\sum_kq_k|R_{jk}|<\infty
\tag{11}
\]

for every row. Therefore all sums below are legitimate. For `j<=N`,

\[
(M_Nq^{(N)}-q^{(N)})_j
=\sum_{k=0}^NR_{jk}q_k
=-\sum_{k>N}R_{jk}q_k.
\tag{12}
\]

Every omitted coefficient has `q_k>0` and every off-diagonal `R_{jk}<0`, so (12) is strictly positive. This proves (3).

PF-276 also proves that `M_N` is a finite Stieltjes matrix, hence `S_N=M_N^{-1}` is entrywise nonnegative; the strict off-diagonal connectivity makes it positivity improving. Applying `S_N` to

\[
M_Nq^{(N)}=q^{(N)}+d_N
\tag{13}
\]

gives

\[
q^{(N)}=S_Nq^{(N)}+S_Nd_N,
\tag{14}
\]

which is (4). The important interpretation is exact: **finite-section `q`-dissipation is not intrinsic Robin damping. It is flux into rows that the Galerkin section omitted.**

## 2. Conjugating by the conserved weight exposes a sub-Markov kernel

For any finite vector `a`, positivity gives the coordinatewise bound

\[
|S_Na|\le S_N|a|.
\tag{15}
\]

Since `S_N` is symmetric,

\[
\begin{aligned}
\|S_Na\|_{1,q}
&\le\sum_{i,j}q_i(S_N)_{ij}|a_j|\\
&=\sum_j(S_Nq^{(N)})_j|a_j|\\
&\le\rho_N\sum_jq_j|a_j|.
\end{aligned}
\tag{16}
\]

Equation (4) makes every ratio in (6) strictly smaller than one, so `rho_N<1`. Equivalently, if

\[
(\Pi_N)_{ji}=\frac{q_j(S_N)_{ji}}{q_i},
\tag{17}
\]

then

\[
\sum_j(\Pi_N)_{ji}
=\frac{(S_Nq^{(N)})_i}{q_i}<1.
\tag{18}
\]

Thus the PF-276 conserved weight converts the Robin inverse into an ordinary positive **column-substochastic** kernel. The missing column mass is exactly

\[
1-\sum_j(\Pi_N)_{ji}
=\frac{(e_N)_i}{q_i},
\tag{19}
\]

with `e_N=S_N[-P_NR(I-P_N)q]`. This is a concrete finite-section escape currency for any later return representation that contains the same Robin factor.

## 3. The strict finite-section gap disappears at infinite depth

Fix one source row `i`. PF-276 proves Galerkin convergence

\[
S_N\varphi_i\longrightarrow S\varphi_i
\quad\text{strongly in }\ell^2.
\tag{20}
\]

All coefficients are nonnegative, so strong convergence implies coordinate convergence. Fatou's lemma for the weighted counting measure gives

\[
\sum_{j\ge0}q_j(S\varphi_i)_j
\le
\liminf_{N\to\infty}
\sum_{j=0}^Nq_j(S_N\varphi_i)_j.
\tag{21}
\]

The left side is exactly `q_i` by PF-276's conserved weighted mass, while (6) with `a=\varphi_i` gives the opposite upper bound

\[
\sum_{j=0}^Nq_j(S_N\varphi_i)_j\le q_i.
\tag{22}
\]

Hence (7) follows. Since `rho_N` is at least the weighted column ratio for this fixed `i`,

\[
1\ge\rho_N
\ge
\frac{1}{q_i}\sum_{j=0}^Nq_j(S_N)_{ji}
\longrightarrow1,
\tag{23}
\]

which proves (8).

This rules out a tempting but false closure of the accepted return clue. Each finite truncation has a strict contraction constant, but that constant is a truncation artifact and necessarily degenerates to one. A proof of the complete response cannot take “every finite return matrix has norm `<1`” and silently promote it to a depth-uniform Neumann-series bound.

## 4. The complete Robin normalization is conservative in `q`

PF-276 gives, for each basis source,

\[
\sum_jq_jS_{ji}=q_i.
\tag{24}
\]

Therefore for finitely supported `a`,

\[
\|Sa\|_{1,q}
\le\sum_i|a_i|\sum_jq_jS_{ji}
=\|a\|_{1,q}.
\tag{25}
\]

Because `q_j` is bounded below away from zero on each parity chain, `ell^1(q)` embeds continuously into `ell^2`; completion therefore extends the Hilbert-space inverse consistently to all of `ell^1(q)`. For `a>=0`, Tonelli and (24) give equality in the weighted mass, proving (9). In the conjugated coordinates (10), (24) becomes

\[
\sum_j\Pi_{ji}=1.
\tag{26}
\]

The same weight `q` is selected by the fixed Jacobi zero mode and does not depend on `s` or `r`, so every complete fixed-axis Robin normalization in this family is a contraction for the **same** weighted coefficient norm. Finite compositions therefore cannot increase the PF-296 source moment. On nonnegative coefficient vectors they preserve it exactly.

This statement is deliberately narrower than a theorem about the complete mixed response. The geometric transports, neighboring-pant Schur elimination, physical low/high projections, source injection, and support/end completion are separate maps. They may change the relevant coefficient currency or create/lose `q`-mass. PF-297 only removes the Robin inverse itself as a possible source of weighted-moment amplification.

## 5. Consequence for the accepted source-weighted return clue

The accepted clue asks for a physical finite-section equation of the form

\[
a=f+Ta
\tag{27}
\]

and a source-adapted positive Green-potential or superharmonic bound. PF-297 supplies one exact local ingredient and one exact obstruction:

- **ingredient:** whenever a return word contains a fixed-axis Robin normalization, that factor is `ell^1(q)`-nonexpansive; in finite sections its exact mass loss is the tail flux (3)--(4);
- **obstruction:** Robin normalization alone cannot give a depth-uniform strict contraction, because its finite-section constants converge to one and the complete map conserves `q`-mass.

Thus the clue's next gate becomes sharper. Derive the actual mixed `T` and locate the first factor at which either (a) the physical forcing is quantitatively compensated by the finite escape, (b) the physical `P/H` split or support loss supplies a genuine additional discount, or (c) mixed/reassembly dynamics amplify or change the `q` currency. A bounded source-adapted potential may still exist even with return norm one; PF-297 says only that its proof cannot come from a uniform Robin contraction gap.

This also separates two nearby mechanisms. [[research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain|PF-279]] shows that unprojected reservoir extension can amplify a complete spatial cut despite a small local crossing coefficient. [[research/prime_flute/findings/PF-280-one-sided-frequency-decoupled-schur-transfer-is-reservoir-stable|PF-280]] shows that after a legitimate physical `P/H` split the surviving mixed corner is instead controlled by a one-sided dressed transfer. PF-297 concerns the fixed-axis Robin inverse inside that architecture; it neither reproduces PF-279's reservoir amplifier nor proves the unresolved PF-280 dressed-transfer estimate.

## Prior art and novelty audit

The finite-dimensional matrix principle is classical. Ronald L. Smith, *M-Matrices whose Inverses are Stochastic*, SIAM Journal on Algebraic and Discrete Methods 2 (1981), no. 3, 259--265, DOI `10.1137/0602028`, studies M-matrices whose inverses are stochastic. Standard M-matrix theory already contains inverse positivity and stochastic/substochastic normalizations. No novelty is claimed for those general facts or for the elementary weighted-`ell^1` norm calculation.

The project-specific content is the identification supplied by PF-276: the Prime-Flute fixed-axis Robin family has one explicit, parameter-independent generalized Jacobi weight `q` for which the complete inverse conserves source mass, while every Galerkin compression loses exactly the omitted-tail flux. Combining that structure with PF-276's Galerkin convergence proves the **collapse of every finite-section contraction gap as depth grows**. That is the new route-level information needed by the accepted PF return-potential question.

A structure-directed literature audit found the expected M-matrix/stochastic-inverse theory and no basis for treating the abstract sub-Markov statement as new. The Prime-Flute specialization and its consequence for the current mixed-response proof strategy are derived here from persisted PF identities rather than imported as an external theorem.

## Boundaries and falsification

1. **Fixed-axis Robin factor only.** PF-297 does not derive the complete `T` in (27), identify the physical forcing `f`, or prove the factorization required by PF-296.
2. **A left mass currency, not a Green majorant.** Column-substochasticity controls weighted `ell^1` mass. It does not by itself construct the source-adapted right superharmonic/excessive vector required to sum a nearly conservative Green potential.
3. **No spectral-gap claim.** `rho_N->1` is a weighted operator-norm statement. It does not by itself identify an eigenvector, prove that the spectral radius tends to one, or construct a physical long-lived mode.
4. **No converse from moment growth.** Failure of a weighted-moment bound would not imply a positive PF-290 shorting deficit; cancellations may remain.
5. **No conflict with PF-279.** PF-279's extension-mass amplification occurs in a larger unprojected Schur completion. PF-297 isolates only the Robin inverse and does not bound all surrounding extension maps.
6. **No weak-trace conclusion.** Nonexpansion of this coefficient factor does not prove compactness, weak `S_1`, scattering equivalence, a determinant statement, a zeta-zero relation, the critical line, or RH.
7. **Direct falsification target.** An error must occur in PF-276's absolute generalized identity `Rq=0`, inverse positivity, weighted column conservation, or Galerkin convergence, or in the finite-dimensional deduction (12)--(23). No new prime-distribution input is used.

## Consequence for the research line

The `q` weight is now more than a row-by-row synthesis cost: it is an exact **nonamplifying currency for the canonical fixed-axis Robin normalization**. This closes one ambiguity in the accepted return-potential investigation. Repeated Robin inversion cannot be blamed for source-moment growth, but neither can its finite-section strictness be used as the missing return discount.

The next useful calculation is therefore the actual `P/H`-split neighboring-pant return/reassembly map in PF-296 source coordinates. Its action on the `q` currency should be measured relative to the explicit tail-loss vector `e_N` in (4), not against an assumed depth-uniform contraction constant. A positive result must show a source/escape balance or an additional physical loss; a negative result should identify the first concrete mixed factor that destroys `q`-nonexpansion or creates a persistent PF-290 deficit.