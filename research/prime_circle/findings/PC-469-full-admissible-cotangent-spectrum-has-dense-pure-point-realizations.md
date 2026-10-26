# PC-469 — The full admissible cotangent spectrum has dense pure-point realizations

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE. Every nonempty cylinder of the prime-admissible support hull contains an infinite support whose unchanged Cauchy operator has a complete eigenvector basis and the entire PC-466 limiting spectrum as essential spectrum. The construction first removes finite block resonances by admissible extensions, then makes successive eigenbasis rotations summable. This supplies a pure-point counterpart to PC-468's residual purely singular-continuous realizations. Trace-class smallness alone does not prove this result. No canonical center selection, zeta-zero identification, RH implication, or historical-priority claim is made.

## 1. Object and theorem

Let
\[
\mathcal A=\{S\subset\mathbb Z:|S\bmod p|<p\text{ for every prime }p\},
\qquad
(A_S)_{ab}=\begin{cases}i/[\pi(a-b)],&a\ne b,\\0,&a=b,\end{cases}
\tag{1}
\]
where `A_S` acts on the retained space `ell^2(S)`. The hull has the product topology inherited from `{0,1}^Z`. Put
\[
\Sigma=\overline{\bigcup_{F\text{ finite nonempty admissible}}\sigma(A_F)},
\qquad \beta=\sup_F\|A_F\|.
\tag{2}
\]
The boundedness `||A_S||<=beta`, moving-center realization, and compactness of `Sigma` are established in [[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]]. The full finite cotangent spectra converge to `Sigma` by [[research/prime_circle/findings/PC-466-full-primorial-cotangent-spectra-converge-to-the-admissible-pattern-spectrum]].

**Theorem.** Given a finite window `W`, an admissible `F_0 subset W`, and `epsilon>0`, there is an infinite `S in A` such that
\[
S\cap W=F_0,\qquad
\boxed{\quad\sigma(A_S)=\sigma_{\rm ess}(A_S)=\Sigma,
\qquad \mathcal H_{\rm pp}(A_S)=\ell^2(S).\quad}
\tag{3}
\]
Moreover, `S` is a disjoint union of finite even-cardinality admissible blocks `G_j` for which
\[
D=\bigoplus_{j\ge1}A_{G_j},\qquad
A_S=D+K,\qquad K=K^*\in\mathcal S_1,\qquad \|K\|_1<\epsilon.
\tag{4}
\]
There is a norm-convergent product of unitaries, each arbitrarily close to the identity at its prescribed summable tolerance, carrying the block eigenbasis to an eigenbasis of `A_S`. The resulting diagonal eigenvalues may differ from those of `D`.

Thus full-spectrum pure-point realizations are **dense** in the admissible hull. In contrast, [[research/prime_circle/findings/PC-468-generic-admissible-cotangent-limits-are-purely-singular-continuous]] supplies a dense `G_delta` of full-spectrum purely singular-continuous realizations. The pure-point family here is consequently meager, despite being dense. Neither conclusion selects a source-forced moving center.

Pure point means a complete orthonormal eigenbasis, not a discrete spectral set. The closed set `Sigma` is perfect by [[research/prime_circle/findings/PC-467-admissible-cotangent-spectrum-is-perfect-and-has-a-purely-singular-realization]]. Its realization in (3) is the closure of countably many eigenvalues and has no isolated spectral points. We do not claim eigenvalue simplicity, exclusion of a zero eigenvalue, or a spatial decay rate for the limiting eigenvectors.

## 2. A finite extension can avoid every prescribed nonzero eigenvalue

For a finite set of distinct real coordinates `F`, put `X=diag(a:a in F)` and `e=(1,...,1)^T`. The classical Cauchy commutator is
\[
[X,A_F]=\frac i\pi(ee^*-I).
\tag{5}
\]
Its expectation in an eigenvector gives `|e^*v|^2=||v||^2`. Hence all eigenvalues are simple. Complex conjugation sends `A_F` to `-A_F`, so its spectrum is symmetric; when `|F|` is even, simplicity and symmetry exclude zero.

For a new real coordinate `b notin F`, a second diagonal commutator gives
\[
\left|\sum_{a\in F}\frac{v_a}{b-a}\right|^2
=\sum_{a\in F}\frac{|v_a|^2}{(b-a)^2}>0
\tag{6}
\]
for every nonzero eigenvector `v` of `A_F`. Indeed, with `d_a=(b-a)^{-1}` and `R=diag(d_a)`,
`[R,A_F]=(i/pi)(dd^*-diag(d_a^2))`; its eigenvector expectation is zero. In the eigenbasis of `A_F`, the enlarged matrix is an arrowhead with every coupling nonzero. Evaluation of its characteristic polynomial at each old simple eigenvalue proves
\[
\sigma(A_{F\cup\{b\}})\cap\sigma(A_F)=\varnothing.
\tag{7}
\]
These finite identities and their strict-interlacing consequence are reconstructed in PC-467; simplicity and the eigenvector-sum identity have the Preissmann–Lévêque prior art listed below.

Now fix a finite set `E subset R\{0}`. For `lambda in E`, the function
\[
f_\lambda(b)=\det(\lambda I-A_{F\cup\{b\}})
\tag{8}
\]
is rational in the real variable `b`, away from the finitely many old coordinates. If `lambda in sigma(A_F)`, (7) says it is never zero there. Otherwise,
\[
\lim_{b\to+\infty}f_\lambda(b)
=\lambda\det(\lambda I-A_F)\ne0.
\tag{9}
\]
Thus it is not the zero rational function and has only finitely many real zeros. This is where `0 notin E` is essential: an odd-dimensional real skew-symmetric matrix, and hence its Hermitian multiple `i/pi`, has a forced zero eigenvalue.

For an admissible integer `F` of size `n`, select `a_0 in F` and
\[
Q=\prod_{p\le n+1}p,\qquad b=a_0+kQ>\max F.
\tag{10}
\]
Then `F union {b}` is admissible: at small primes the new point repeats an occupied residue, and primes larger than `n+1` cannot be covered. This progression is unbounded and avoids the finite exceptional set in (8) for all sufficiently large `k`. Also
\[
\left\|A_{F\cup\{b\}}-(A_F\oplus0)\right\|
=\frac1\pi\left(\sum_{a\in F}(b-a)^{-2}\right)^{1/2}\longrightarrow0.
\tag{11}
\]

It follows that, for any nonempty finite admissible `F`, any finite `E subset R\{0}`, and any `delta>0`, there is an even-cardinality admissible extension `T superset F` such that
\[
\sigma(A_T)\cap E=\varnothing,
\qquad
\sup_{\lambda\in\sigma(A_F)}\operatorname{dist}(\lambda,\sigma(A_T))<\delta.
\tag{12}
\]
Add one point if `|F|` is odd and two if it is even. At each step choose (10) sufficiently far to avoid `E` and make the error in (11) less than `delta/2`; Hermitian spectral perturbation gives (12). All auxiliary points can lie outside any prescribed finite window. The one-way spectral approximation is sufficient; the auxiliary near-zero eigenvalues are allowed.

## 3. The finite perturbation estimate used in the induction

Let `B` be an `N`-dimensional Hermitian matrix with simple eigenvalues and minimum eigenvalue gap `g>0`. For a Hermitian perturbation `E` with `e=||E||<g/4`, order the eigenvalues of `B+E` against those of `B`. Weyl's finite perturbation bound puts each new eigenvalue within `e` of its old value.

If `v_j` and `w_j` are the paired unit eigenvectors, projection of the new eigenvector equation onto the complement of `v_j` gives
\[
\|(I-v_jv_j^*)w_j\|\le\frac e{g-e}.
\tag{13}
\]
Choose the phase so `v_j^*w_j>=0`. Then
\[
\|w_j-v_j\|\le\frac{\sqrt2 e}{g-e}<\frac{3e}{g}.
\]
The unitary `V` mapping the old orthonormal eigenbasis to the new one satisfies
\[
\|V-I\|\le\|V-I\|_{\rm HS}<\frac{3\sqrt N e}{g}.
\tag{14}
\]
This elementary instance of classical gap-controlled eigenvector perturbation is proved here to make the stage-dependent constants explicit. There is no uniform lower bound on gaps across the induction.

## 4. Admissible blocks with disjoint spectra and summable rotations

First enlarge `F_0` outside `W` to a nonempty even admissible `G_1`, using (10). If `F_0` is empty, start with a singleton outside `W` and extend once. Set `U_1=G_1`. No later block will meet `W`.

Enumerate all nonempty finite admissible integer shapes modulo translation as `F_j`, `j>=2`, with every shape repeated infinitely often. Choose positive sequences
\[
\delta_j\downarrow0,\qquad \sum_{j\ge2}\kappa_j<\epsilon,
\qquad \sum_{j\ge2}\eta_j<\infty.
\tag{15}
\]
The last sum may be made arbitrarily small. Suppose `U_(j-1)` has been constructed and has even cardinality. Its Cauchy spectrum is simple and excludes zero. Apply (12) to `F_j` with
\[
E=\sigma(A_{U_{j-1}})
\]
to obtain an even admissible `T_j` approximating the target block spectrum within `delta_j` and avoiding all of `E`. Thus
\[
B_j=A_{U_{j-1}}\oplus A_{T_j}
\tag{16}
\]
has simple spectrum with some finite positive minimum gap `g_j`.

Translate `T_j` to `G_j=t_j+T_j`, preserving admissibility of the union. Explicitly, put `n=|U_(j-1)|+|T_j|`. For each prime `p<=n`, choose residues `r_p` and `s_p` omitted respectively by the two sets and impose
\[
t_j\equiv r_p-s_p\pmod p.
\tag{17}
\]
CRT supplies a translation progression; every resulting union misses `r_p`. Larger primes are excluded by cardinality. Arbitrarily large positive members of that progression place the new block beyond `W` and every preceding block.

The cross-block perturbation `E_j=A_(U_(j-1) union G_j)-B_j`, interpreted in the translated block coordinates, satisfies
\[
\|E_j\|\le\|E_j\|_1
\le\frac{2|U_{j-1}|\,|T_j|}{\pi d_j}\longrightarrow0,
\qquad d_j=\operatorname{dist}(U_{j-1},G_j).
\tag{18}
\]
The trace-norm bound sums both directions of all matrix-unit entries. Choose the translation only **after** fixing `T_j` and `g_j`, sufficiently far that
\[
\|E_j\|_1<\kappa_j,\qquad
\|E_j\|<g_j/4,\qquad
3\sqrt{|U_j|}\,\|E_j\|/g_j<\eta_j,
\tag{19}
\]
where `U_j=U_(j-1) union G_j`. Equations (14) and (19) give a unitary `V_j` on `ell^2(U_j)` carrying the eigenbasis of (16) to one of `A_(U_j)`, with `||V_j-I||<eta_j`.

No diagonal potential, reweighting or deletion of an actual Cauchy interaction is used. Finite spectral resonances are removed by adding admissible coordinates; translation then makes the remaining genuine interactions small relative to that stage's gap.

Let `S=union_j U_j`. It is admissible: coverage of all residues modulo a prime would have finitely many witnesses contained in one `U_j`. Each block is nonempty, so `S` is infinite. Summing (18) over the stage of the later endpoint counts every cross-block entry exactly once in each direction and gives (4).

## 5. Norm convergence of the conjugations proves completeness

Fix an orthonormal eigenbasis on each block and take their union as a basis `B_0` of `ell^2(S)`. Extend each `V_j` by the identity off `U_j` and put
\[
P_1=I,\qquad P_j=V_jP_{j-1}.
\tag{20}
\]
Inductively, `P_j` sends the basis vectors of the first `j` blocks to an eigenbasis of `A_(U_j)` and leaves all future block basis vectors unchanged. Indeed, the old images together with the new block basis are an eigenbasis of (16), precisely the basis transported by `V_j`.

Since `||P_j-P_(j-1)||<eta_j`, (15) gives a norm limit `P`. The adjoints converge in norm as well, so `P^*P=PP^*=I`: the limit is a surjective unitary, not just an isometry. This rules out loss of eigenvectors to infinity.

On the same final Hilbert space define
\[
H_j=A_{U_j}\oplus\bigoplus_{k>j}A_{G_k}.
\tag{21}
\]
Each `P_j^*H_jP_j` is diagonal in the **fixed complete** basis `B_0`. All missing interactions in `H_j` have a later block index `k>j`, so
\[
\|A_S-H_j\|_1\le\sum_{k>j}\kappa_k\longrightarrow0.
\tag{22}
\]
Together with norm convergence of `P_j` and the common operator bound, this implies
\[
P_j^*H_jP_j\longrightarrow P^*A_SP
\quad\text{in operator norm}.
\tag{23}
\]
The algebra of operators diagonal in a fixed basis is norm closed. Hence `P^*A_SP` is diagonal, and `P B_0` is a complete orthonormal eigenbasis of `A_S`. This proves the pure-point assertion in (3).

The proof does not infer atomicity from trace-class perturbation, convergence of eigenvalue sets, or weak limits of finite atomic measures. Nor does it track only a few eigenvectors and assume completeness: (20)–(23) control the entire basis.

## 6. Recovering the entire spectral set

Every `G_j` is admissible, so the block-diagonal operator `D` has spectrum contained in `Sigma`. For each finite admissible `F` and each `lambda in sigma(A_F)`, infinitely many distinct blocks approximate that eigenvalue by (12), with errors tending to zero. Their block eigenvectors form a singular Weyl sequence for `D` at `lambda`. Closedness of essential spectrum then gives
\[
\sigma(D)=\sigma_{\rm ess}(D)=\Sigma.
\tag{24}
\]
The compact perturbation in (4) preserves essential spectrum. To exclude additional isolated spectral points, use the general finite-compression argument: for any `lambda in sigma(A_S)` take finite-support unit approximate eigenvectors `v`, and set `F=supp(v)`. Then
\[
\operatorname{dist}(\lambda,\sigma(A_F))
\le\|(A_F-\lambda)v\|
\le\|(A_S-\lambda)v\|.
\tag{25}
\]
Thus `sigma(A_S) subset Sigma`. Together with (24) and Weyl invariance this proves the spectral equalities in (3).

Zero extension to `ell^2(Z)` only adds a zero eigenspace, and `0 in Sigma`. PC-465 therefore realizes this operator as a strong moving-center limit along any prescribed primorial cutoffs tending to infinity and positive integer refinements. The same underlying finite spectra admit both this limit and PC-468's purely singular-continuous limits; spectral-set convergence does not select the limiting spectral-measure type.

## 7. Mathematical delta, controls and prior art

PC-467 constructs a full-spectrum trace-class perturbation of finite blocks but deliberately leaves its atomic versus singular-continuous decomposition open. PC-468 resolves a separate generic singular-continuity question by **resonant duplication**, which splits and spreads coordinate atoms. Here the added finite vertices remove those resonances before gluing; summable whole-basis rotations then produce a different, pure-point realization. This does not reclassify the particular support constructed in either preceding finding.

The mechanism is not specific to actual prime occurrence. Its inputs are finite Cauchy simplicity/noncancellation, admissibility-preserving far extensions and translations, uniform boundedness, and a summable separation budget. Any support class satisfying those properties admits the corresponding construction. Arithmetic is retained in the admissible shape set and its identification with the original cotangent limit. No claim is made that all such classes have the same `Sigma`.

Closest prior art and exact roles:

- E. Preissmann and O. Lévêque, *On generalized weighted Hilbert matrices*, **Pacific J. Math. 265** (2013), 199–219, DOI `10.2140/pjm.2013.265.199`, [paper](https://msp.org/pjm/2013/265-1/pjm-v265-n1-p09-p.pdf). Corollary 1 and Lemma 7 supply finite simplicity and the eigenvector-sum identity. The rational-parameter avoidance argument (8)–(12) is derived explicitly here from the stronger extension noncancellation already proved in PC-467.
- C. Davis and W. M. Kahan, *The Rotation of Eigenvectors by a Perturbation. III*, **SIAM J. Numer. Anal. 7** (1970), 1–46, [DOI](https://doi.org/10.1137/0707001). Gap-controlled eigenvector rotation is classical. Equations (13)–(14) give all the finite estimates actually used, without relying on a stronger uniform or infinite-dimensional gap theorem.
- L. Amour and J.-C. Guillot, *Examples of Discrete Operators with a Pure Point Spectrum of Finite Multiplicity*, **J. Math. Anal. Appl. 229** (1999), 170–183, [DOI](https://doi.org/10.1006/jmaa.1998.6152). The publisher's abstract describes KAM constructions of discrete pure-point operators with dense point spectra. This is neighboring prior art for block diagonalization and dense pure-point spectral sets, not a theorem applied to this unchanged Cauchy kernel or the prime-admissible hull. No uninspected theorem from that paper is used.
- G. Teschl, *Mathematical Methods in Quantum Mechanics*, 2nd ed., AMS GSM **157** (2014), [author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), Lemmas 6.17–6.18 and Theorem 6.19. These provide the classical singular Weyl criterion and compact-perturbation invariance used in (24); (25) supplies the separate exclusion of additional spectrum.

Local duplication checks covered PC-465–PC-468 and targeted searches for full-spectrum pure-point realizations, nonresonant blocks and complete eigenbases. Structural literature searches covered generalized Hilbert/Cauchy matrices, sparse blocks, dense pure-point spectrum and gap-controlled diagonalization. The contribution recorded is the admissible finite-extension and gluing construction for this exact family, not a new general localization theorem or an assertion of historical novelty.

The proof gives no exponential or power-law eigenvector localization, no classification of all admissible supports, no absolutely continuous realization, and no information about the gaps or Lebesgue measure of `Sigma`. The choices can be extremely sparse and noncanonical. Full essential-spectrum recovery plus pure-point spectral measures is not a Hilbert–Pólya identification.

## 8. Validation and evidence boundary

The theorem is an analytic derivation, not Lean-verified or independently adversarially approved. A deterministic standard-library Python audit used exact rational characteristic polynomials of the real skew Cauchy matrices, polynomial gcds, exact CRT, and system LAPACK `zheev` through `ctypes` for the floating-point diagnostics. From **26** admissible shapes of sizes one through four in `[0,12]`, it selected **6** even old shapes and every third target shape, checking **84** extension steps and **54** subsequent nonresonant admissible gluings. Polynomial gcds verified exact spectral disjointness at each extension, including initially identical/resonant blocks; even blocks had nonzero determinant. The common factor `i/pi` does not change whether two spectra intersect.

For the **348** paired finite eigenvectors, phase-adjusted basis rotation satisfied (14); the maximum ratio of its measured Hilbert–Schmidt change to the displayed bound was below `0.118`. All tested eigenvalue perturbations satisfied the operator-norm bound, and the assembled matrices were exactly Hermitian in the numerical representation. These checks audit finite parity, avoidance, CRT, signs and perturbation normalization; they do not prove convergence of the infinite basis. The proof of that passage is (20)–(23). Scratch code and output remain under `/tmp`, outside Git.

The decisive analytic checks are: exclude zero from the forbidden finite spectrum; avoid resonances before choosing the next translation; use the actual new finite gap without assuming a uniform one; include every cross-block interaction in the summable trace budget; prove norm convergence of both the unitary products and their adjoints; diagonalize in one fixed complete basis; repeat all target shapes; and separately exclude off-set spectrum. Each is explicit above.

No compute or formalization executor is enrolled. The finite spectral ingredients are classical and proved here; the additional theorem rests on an infinite separation/diagonalization construction, with no distinct bounded formalization-fertility target asserted.
