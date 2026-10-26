# PC-471 — Compatible root phases retain the full spectrum but generically collapse

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. Requiring the moving centers to be one compatible residue system strictly reduces the admissible support class, but does not remove full-spectrum cotangent limits. Those exceptional phases are dense, while the product-uniform law and Baire category on the compatible rooted phase space both select the zero operator. The coding is classical B-free window coding; the additional boundary concerns its exact image and the unchanged Prime-Circle Cauchy operator. No historical-priority claim, canonical exceptional phase, spectral-type classification, or RH implication is made.

## 1. The compatibility restriction and its exact limit

Put
\[
d_y=\prod_{p\le y}p\quad(y\ge2),\qquad
H_0=\prod_p(\mathbb Z/p\mathbb Z)^{\times}.
\tag{1}
\]
Give `H_0` its compact product topology and the product `m_0` of uniform probabilities on the nonzero residues. A phase `a=(a_p)` specifies, by CRT, the unique retained center `c_y mod d_y` satisfying `c_y=a_p mod p` for all `p<=y`. Thus
\[
c_z\equiv c_y\pmod {d_y}\quad(z\ge y).
\tag{2}
\]
This is compatibility of **integer center labels under conductor reduction**. It is an additional selection constraint on PC-465, not an assertion that every geometric refinement prescribes such a center. No compatibility of arbitrary refinement factors is needed below.

For `N=d_y m`, with any integer `m>=1`, choose any lift of `c_y` modulo `N`. Define its centered mask on `I_N={-N/2,...,N/2-1}` and the zero-extended operator on `ell^2(Z)` by
\[
S_{y,m,a}=\{h\in I_N:(c_y+h,d_y)=1\},
\qquad
(K_{y,m,a})_{hk}=
\begin{cases}
\dfrac iN\cot\dfrac{\pi(h-k)}N,&h,k\in S_{y,m,a},\ h\ne k,\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
\]
Write `chi` for the indicator of `S_(y,m,a)`. The choice of lift does not change these offset memberships. The limiting support and operator are
\[
S(a)=\{h\in\mathbb Z:a_p+h\not\equiv0\pmod p\text{ for all }p\},
\qquad
(L_{S(a)})_{hk}=\mathbf1_{h,k\in S(a)}
\begin{cases}i/[\pi(h-k)],&h\ne k,\\0,&h=k.\end{cases}
\tag{4}
\]
In particular `0 in S(a)`. Let
\[
\mathcal A_0=\{S\subset\mathbb Z:0\in S,\ |S\bmod p|<p\text{ for every prime }p\},
\qquad \mathcal C_0=\{S(a):a\in H_0\}.
\tag{5}
\]
Keep the existing compact spectral set
\[
\Sigma_{\rm adm}=
\overline{\bigcup_{F\text{ finite nonempty admissible}}\sigma(A_F)},
\qquad (A_F)_{hk}=i/[\pi(h-k)]\ (h\ne k),\quad (A_F)_{hh}=0,
\tag{6}
\]
where `A_F` acts on the retained space `ell^2(F)`. This is the full finite spectral limit of [[research/prime_circle/findings/PC-466-full-primorial-cotangent-spectra-converge-to-the-admissible-pattern-spectrum]].

**Theorem.**

1. Every compatible rooted phase has `K_(y,m,a) -> L_(S(a))` strongly as `y -> infinity`, uniformly over refinements on each fixed input vector. The augmented convention `K+chi chi*/N` has the same limit.
2. `C_0` is a proper dense subset of `A_0`. It contains every finite member of `A_0`, but not every infinite member.
3. The set `Z_0={a:S(a)={0}}` is a dense `G_delta` of full `m_0` measure. It is exactly the continuity set of the support map `a -> S(a)` into the product topology. At all these phases the limiting operator is zero.
4. Every nonempty phase cylinder contains an `a` for which `S(a)` is infinite and
   \[
   \boxed{\quad\sigma(A_{S(a)})=\sigma_{\rm ess}(A_{S(a)})=\Sigma_{\rm adm}.\quad}
   \tag{7}
   \]
   Here `A_(S(a))` is the restriction of (4) to its retained space. The same equality holds after zero extension.

Thus full-spectrum phases are dense but meager and `m_0`-null. Compatibility eliminates some attainable supports without eliminating the spectral-set ambiguity. Neither (7) nor density specifies atomic, absolutely continuous or singular continuous spectral type.

## 2. Compatible masks converge, but their image is not the whole hull

Each fixed offset surviving all primes remains in every sufficiently large centered interval. Every other offset is killed permanently by one witnessing prime. Hence the masks in (3) converge pointwise to (4). The column estimate from [[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]], §3, is
\[
\sum_{|h|>R}|(K_{y,m,a})_{hk}|^2
\le\frac2{\pi^2(R-|k|)}\qquad(R>|k|),
\tag{8}
\]
and holds also for `L_(S(a))`. Fixed-window convergence, (8), and the uniform norm bound `||K||<=1` prove strong convergence. The membership decisions and the lower bound `N>=d_y` make this uniform in `m` for each fixed vector. The augmentation has norm `phi(d_y)/d_y -> 0`.

For finite admissible `F` containing zero, enumerate `Z\F`. To each hole `b` assign a distinct prime
\[
p_b>\max\{|b-f|:f\in F\},\qquad p_b>|F|,
\]
and prescribe the forbidden offset residue `r_(p_b)=b mod p_b`. This removes `b` without removing any `f in F`. At every unassigned prime choose a residue outside `F mod p`. All forbidden residues are nonzero because `0 in F`. Taking `a_p=-r_p` gives `S(a)=F` exactly. Finite truncations of every `S in A_0` are admissible and converge to `S`, so `C_0` is dense.

There is, however, an explicit missing infinite support:
\[
S_* =\{0\}\cup\{2+n!:n\ge3\}.
\tag{9}
\]
Modulo `2` it occupies only zero; modulo `3` it occupies only `0,2`. For a prime `p>=5`, the terms with `n>=p` are all `2 mod p`, while there are only `p-3` earlier indices `3<=n<p`. Including the root and tail residue gives at most `p-1` residues. Therefore `S_* in A_0`.

For **every** prime `p`, some member of `S_*` is congruent to `2 mod p`. Any forbidden residue preserving all of `S_*` must consequently differ from `2 mod p`. Thus every `S(a)` containing `S_*` must contain `2`. But `2 notin S_*`, proving
\[
S_*\notin\mathcal C_0.
\tag{10}
\]
More generally, an offset whose residue lies in `S mod p` at every prime cannot be removed by a one-forbidden-residue-per-prime sieve preserving `S`. This is a necessary condition, not a claimed sufficient characterization of the coding image.

PC-465's arbitrary moving centers realize (9); no fixed compatible phase realizes it. This distinction also survives at the operator level: on a rooted support with at least two points, the nonzero entries in column zero identify exactly its nonroot members. In particular adding the forced point `2` changes the operator.

## 3. Generic and product-uniform compatible roots collapse

For a fixed `h!=0`, write `E_h={a:h in S(a)}`. It is closed. It has empty interior: in any cylinder fixing finitely many prime coordinates, choose a new prime `p` not dividing `h` and set `a_p=-h mod p`. This is a nonzero allowed phase and kills `h`. Consequently
\[
Z_0=\bigcap_{h\ne0}(H_0\setminus E_h)
\tag{11}
\]
is a dense `G_delta` by Baire's theorem.

Independence of the prime coordinates gives
\[
m_0(E_h)=\prod_{p\nmid h}\frac{p-2}{p-1}=0.
\tag{12}
\]
If `h` is odd, the `p=2` factor is already zero. Otherwise divergence of the sum of prime reciprocals makes the product zero; deleting the finitely many prime divisors of `h` does not alter this conclusion. Countably many nonzero offsets prove `m_0(Z_0)=1`.

This is the inverse-limit law of uniform **retained** centers: its marginal modulo `d_y` is uniform on the units. It is not ordinary additive Haar measure conditioned on a positive-probability infinite event. In the ambient product `prod_p Z/pZ`, retaining zero has probability `prod_p(1-1/p)=0`.

At `a in Z_0`, each of finitely many nonroot offsets in a requested window has a finite prime witness killing it. Fix those phase coordinates; the whole window is then fixed, proving continuity. At `a notin Z_0`, choose `h!=0` in `S(a)`. A new coordinate can kill it in every cylinder about `a`, proving discontinuity. This proves the exact continuity-set assertion.

The zero operator is therefore selected both almost surely and on a residual set of **phase parameters**. This is compatible with PC-468's residual full-spectrum behavior in the different **support-hull topology**: the coding has a proper nonclosed image and is discontinuous at every phase with a nontrivial rooted support. Genericity is not transported by it. No operator-norm convergence of the original finite matrices is implied.

## 4. Buffered patterns can be installed without changing old phases

The missing point in applying PC-466 directly is that its admissible gluing can choose a new omitted residue at every stage. Here each already assigned prime must retain its old residue forever.

Maintain a finite admissible occupied set `U` containing zero, a finite prime set `J`, and prescribed nonzero forbidden residues `r_p` for `p in J` avoided by `U`. Also maintain finitely many protected windows whose holes are already excluded by these phases. Start with `U={0}` and any specified nonempty rooted phase cylinder.

Given a finite nonempty admissible shape `F`, let `n=|U|+|F|`. At each `p in J`, admissibility of `F` permits a translation residue `t_p` with
\[
r_p\notin t_p+F\pmod p.
\tag{13}
\]
At each `p<=n` not yet in `J`, choose a residue `r_p` missing from `U`, then a `t_p` satisfying (13). CRT solves all these translation constraints simultaneously. Choose its representative `t` arbitrarily far to the right, so a desired finite buffer window about `t+F` lies beyond all previous occupied points and protected windows.

The union `U'=U union(t+F)` avoids the specified residue at every prime in `J` and every prime `p<=n`. For larger primes its cardinality is at most `n<p`. Thus `U'` is admissible. Record the newly chosen phases at `p<=n`.

For each hole `b` in the new buffer window outside `t+F`, choose a different as-yet-unassigned prime
\[
q_b>\max_{u\in U'}|b-u|,\qquad q_b>|U'|,
\]
and set `r_(q_b)=b mod q_b`. The window was disjoint from old `U`, so none of these holes belongs to `U'`. These phases kill every new hole and preserve every occupied point, including zero. Later stages preserve those phase assignments, hence cannot refill an old hole. This proves the required extension lemma with **frozen** old residues.

Now enumerate all finite nonempty admissible shapes modulo translation, each infinitely often, as `F_j subset [-b_j,b_j]`. At step `j` install a copy `G_j=t_j+F_j` in the exact protected window `t_j+[-R_j,R_j]`, where
\[
R_j>b_j+j^2|F_j|+1.
\tag{14}
\]
Place these windows disjointly to the right. The number of retained points tends to infinity, so the rule assigning all primes up to `|U|+|F_j|` eventually assigns every prime. The resulting phase `a` extends the initial cylinder, preserves every `G_j`, and has
\[
S(a)\cap(t_j+[-R_j,R_j])=G_j
\tag{15}
\]
for every `j`. Additional survivors outside the protected windows are allowed and are not discarded.

## 5. All cross-window interactions satisfy the Weyl residual bound

Let `v_j` be a unit eigenvector of `A_(F_j)` with eigenvalue `lambda_j`, translated to `G_j` and zero elsewhere in `ell^2(S(a))`. By (15), its residual vanishes inside the protected window. For each input coordinate in `G_j`, the squared Cauchy tail outside that window is at most `2/[pi^2(R_j-b_j)]`. Summing input columns using `||v_j||_1<=sqrt(|F_j|)` gives
\[
\|(A_{S(a)}-\lambda_j)v_j\|
\le\sqrt{\frac{2|F_j|}{\pi^2(R_j-b_j)}}
<\frac{\sqrt2}{\pi j}.
\tag{16}
\]
This controls all other survivors, not only the deliberately installed blocks.

For each eigenvalue of any fixed finite admissible shape, select the corresponding eigenvector at its infinitely many occurrences. The supports are disjoint, so these unit vectors are orthonormal, and (16) makes them a singular Weyl sequence. Closedness of essential spectrum gives
`Sigma_adm subset sigma_ess(A_(S(a)))`.

Conversely, for any admissible support `S`, a finite-support unit approximate eigenvector at a spectral value `lambda` can be compressed to its finite support `F`. Then
\[
\operatorname{dist}(\lambda,\sigma(A_F))
\le\|(A_S-\lambda)v\|.
\tag{17}
\]
Boundedness and density of finite-support vectors justify their use. Taking residuals to zero shows `sigma(A_S) subset Sigma_adm`, as already proved in PC-466. This proves (7). Zero extension adds only `0`, which is already in `Sigma_adm`.

Since the initial phase cylinder was arbitrary, full-spectrum phases are dense. They lie outside `Z_0`: the admissible pair `{0,2}` supplies the nonzero eigenvalues `+/-1/(2pi)` in (6). Equations (11)--(12) therefore make the full-spectrum phases meager and null. This completes the theorem.

## 6. Mathematical delta, controls and prior art

PC-465 explicitly leaves centers incompatible, PC-466 glues a full-spectrum admissible support without a fixed phase system, and PC-470 classifies change-of-measure costs without imposing consistency of the chosen laws across cutoffs. None of those statements identifies the exact compatible coding image or proves full-spectrum realization while permanently freezing every previously chosen sieve phase. Equations (9)--(10) and (13)--(16) settle this additional selection constraint in opposite directions: some supports disappear, but the full spectral set survives.

The underlying representation is established prior art. S. Kasjan, G. Keller and M. Lemańczyk, *Dynamics of B-free sets: a view through the window*, **International Mathematics Research Notices 2019**, no. 9, 2690--2734, DOI [10.1093/imrn/rnx196](https://doi.org/10.1093/imrn/rnx196), [author manuscript](https://arxiv.org/pdf/1702.02375), §1.1 defines precisely the group, window and coding in (4); Lemma 3.10 characterizes coding continuity by avoidance of the window boundary. Here `B` is all primes, and the retained-root phase space is the product of nonzero residues. The rooted continuity and measure statements are proved directly above rather than imported from a positive-density sieve theorem.

Dymek--Kasjan--Kułaga-Przymus--Lemańczyk, *B-free sets and dynamics*, [author manuscript](https://arxiv.org/pdf/1509.08010), Definition 2.28 and Example 2.45, remain the admissibility anchor: for all primes, the orbit closure of the already-limited prime-free set `{+1,-1}` differs from the admissible hull. Neither that orbit closure nor the closure of a coding image should be substituted for the image itself. The finite-pattern and singular-Weyl spectral mechanism is the same classical one reconstructed in PC-466; the new ingredient needed here is preservation of assigned phases and holes at every gluing stage.

Local duplication searches covered compatible centers, profinite phase coding, residue-closure obstructions and the recent cotangent limit findings. External searches covered B-free window coding, Behrend/admissible dynamics and sieved cotangent spectra. The classification is recorded as a classical-method specialization, not a historically new coding theory or spectral mechanism.

The category argument uses infinitely many independent prime coordinates; the measure argument additionally uses divergence of the reciprocal-prime sum. CRT gluing uses pairwise coprimality and the one-residue admissibility of each finite shape. These hypotheses identify exactly which matched sieve models reproduce the mechanism. Density alone does not reproduce the admissible spectral set, and changing to a summable sieve changes (12). No sign law, coercive estimate or zeta-zero identification follows from compatibility itself.

## 7. Validation and evidence boundary

A standard-library exact-arithmetic audit under `/tmp` checked **14** admissible rooted finite patterns and their hole-killing CRT prescriptions, the complete factorial-witness residue sets for **95** primes through `499`, and **96** exact rooted inclusion probabilities against the finite product in (12). It also performed **144** phase-preserving gluing stages across eight different initial phase cylinders, checking old residues, admissibility, all earlier protected holes and retained points after each stage; coordinates reached 131 digits. These **349** finite diagnostics passed. They verify congruence and normalization details, not the infinite theorem or spectral type.

The proof is analytic and combinatorial, not Lean-verified or independently adversarially approved. Its critical infinite steps are countable hole exclusion, distinction between the coding image and its closure, Baire/product-measure nullity, frozen-phase buffered gluing, and the full-output residual estimate (16). Strong convergence never supplies spectral convergence by itself.

This resolves the bounded question of conductor-compatible root selection. No exceptional phase is selected by the original geometry, and no compute or formalization executor is enrolled. The elementary finite congruences do not by themselves form a separate consequential formalization-fertility target; the result depends on their infinite coding and spectral passage.
