# PC-473 — Compatible root selection has no finite hole certificate

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. Every finite set of unwanted offsets can be excluded by a compatible phase preserving an entire infinite support, while no phase realizes that support exactly. The support can differ by just one point from an exactly compatible support and can be approached by compatible **supersets**. The result realizes a classical infinite-choice obstruction inside the prime-residue coding; it is not a new compactness principle, spectral-type theorem, or RH implication. No historical-priority claim is made.

## 1. The finite-consistency repair fails

Use the forbidden-residue convention of
[[research/prime_circle/findings/PC-471-compatible-root-phases-retain-full-spectrum-but-generically-collapse]]:
\[
C(r)=\{h\in\mathbb Z:h\not\equiv r_p\pmod p\text{ for every prime }p\},
\qquad r_p\ne0,
\qquad \mathcal C_0=\{C(r)\}.
\tag{1}
\]
For a rooted admissible support `S`, put
\[
M_p(S)=(\mathbb Z/p\mathbb Z)\setminus(S\bmod p),\qquad
W_h(S)=\{p:h\bmod p\in M_p(S)\}.
\tag{2}
\]
Admissibility means every `M_p(S)` is nonempty; rooted means `0 in S`, so none contains zero. A phase preserves all of `S` exactly when it belongs to the compact product
\[
R_S=\prod_p M_p(S).
\tag{3}
\]

[[research/prime_circle/findings/PC-472-primewise-separation-does-not-ensure-compatible-root-selection]] gives a primewise-closed support with a **finite** conflict: holes `2,4` require different residues at the same prime. Consider the stronger necessary condition
\[
\boxed{\quad
\forall H\subset\mathbb Z\setminus S\text{ finite},\quad
\exists r\in R_S:\ C(r)\cap H=\varnothing.
\quad}
\tag{4}
\]
Unlike finite-window admissibility, (4) requires preservation of the **whole infinite** `S` in every test.

**Theorem.** There is an infinite rooted admissible `S` such that:

1. `cl_pr(S)=S`, where `cl_pr(S)={h:h mod p in S mod p for every p}`.
2. Condition (4) holds, but `S notin C_0`.
3. `T=S union {2}` belongs to `C_0`.
4. There are `C_j in C_0` with `S subset C_j`, `2 notin C_j`, and `1_(C_j) -> 1_S` pointwise.
5. For the unchanged zero-extended Cauchy operators
   \[
   (L_D)_{hk}=\mathbf1_{h,k\in D}
   \begin{cases}i/[\pi(h-k)],&h\ne k,\\0,&h=k,\end{cases}
   \tag{5}
   \]
   one has `L_(C_j) -> L_S` strongly, although no compatible phase has operator `L_S`.

Thus finite simultaneous-exclusion tests cannot characterize the exact coding image. Even deletion of one nonroot point can leave that image. The last assertion concerns strong topology, not operator norm or spectral convergence.

## 2. The residue data to be realized

We construct an infinite set `A={p_1,p_2,...}` of primes at least five, nonzero residues `r_q` with `r_q != 2 mod q` at **every** prime, and distinct integers `b_j` different from `0,2`. Define
\[
M_q=\begin{cases}
\{r_q,2\bmod q\},&q\in A,\\
\{r_q\},&q\notin A.
\end{cases}
\tag{6}
\]
The two residues in the first case are distinct and nonzero. The construction will give
\[
T=C(r)=S\sqcup\{2\},\qquad
S\bmod q=(\mathbb Z/q\mathbb Z)\setminus M_q,
\tag{7}
\]
and
\[
b_j\equiv r_{p_j}\pmod {p_j},\qquad
b_j\bmod q\notin M_q\quad(q\ne p_j).
\tag{8}
\]
Consequently
\[
W_2(S)=A,\qquad W_{b_j}(S)=\{p_j\}.
\tag{9}
\]
Each `b_j` forces the default choice `r_(p_j)` if it is to be removed while preserving `S`; removing `2` requires changing at least one of those choices. The substantial realization issue is to make (7)--(8) hold at **all primes**, rather than merely at a checked finite prefix.

## 3. A permanent-assignment CRT construction

Maintain finite sets `U` of installed retained points, `J` of assigned primes, and `A_J subset J` of special primes. For each `p in A_J` there is one installed hole `b_p`. Write
\[
B=\{b_p:p\in A_J\},\qquad V=U\cup\{2\}\cup B.
\tag{10}
\]
Initially `U={0}` and `J=A_J=B=empty`. The three parts in (10) are disjoint. Maintain these invariants:

- At an ordinary assigned prime `q in J\A_J`, all of `V` avoids `r_q`.
- At a special prime `p`, `U` and `B\{b_p}` avoid both `2 mod p` and `r_p`; the designated `b_p` equals `r_p mod p`. The point `2` avoids every default residue `r_q`.
- At each unassigned prime `q`, `V mod q` omits at least one residue.
- Assigned residues, special/ordinary designations, and installed points never change.

The initial unassigned-prime invariant holds: `{0,2}` occupies only zero modulo two and at most two residues at every larger prime.

Before a step that will enlarge `V` to at most `n` points, **freeze every unassigned prime `q<=n` as ordinary**, choosing `r_q` missing from the current `V mod q`. The third invariant permits this; the presence of `0,2` makes the chosen residue nonzero and different from `2 mod q`. New points are then chosen to avoid these frozen residues. Any still-unassigned prime exceeds `n`, so cardinality alone preserves its missing-residue invariant.

### Install a new special coordinate and its forced hole

Set `n=|V|+1` and perform the freezing step. Choose an unassigned prime `p>max(n,3)` such that
\[
p\nmid(v-2)\quad(v\in V\setminus\{2\}).
\tag{11}
\]
Only finitely many primes divide these finitely many nonzero integers, so such a prime exists. Choose `r_p` outside `V mod p`, possible because `p>|V|`, and designate `p` special. All old retained points and old forced holes now avoid both residues in (6).

Choose the new `b_p` by CRT:
\[
b_p\equiv r_p\pmod p,\qquad
b_p\equiv0\pmod q\quad(q\in J\text{ previously assigned}).
\tag{12}
\]
Every old missing set avoids zero. Choose a positive representative larger than all existing points and add it to `B`. It avoids every old missing residue, has precisely its intended conflict at `p`, and preserves the unassigned-prime invariant by the freezing bound. This operation can be repeated infinitely often.

### Fill every allowed residue at a specified prime

For a prime `q`, first assign it as ordinary if it is still unassigned. It already has the missing set `M_q` from (6). Let
\[
n=|V|+q-|M_q|
\tag{13}
\]
and freeze all remaining unassigned primes up to `n` as ordinary. For each `v mod q` outside `M_q`, CRT supplies an integer
\[
x_v\equiv v\pmod q,\qquad
x_v\equiv0\pmod p\quad(p\in J\setminus\{q\}).
\tag{14}
\]
Choose distinct positive representatives beyond all old points and install them in `U`. These points avoid the entire current family of missing sets. The new `V` has at most `n` points, so unassigned primes remain admissible. Every allowed residue at `q` now has a retained witness. Later assignments preserve all those witnesses, while the missing residues at `q` remain missing forever.

### Remove every other integer not installed as retained

Process an integer `k!=2`. If `k in U`, retain it. If some already assigned default residue kills `k`, no action is needed. Otherwise `k notin V`: every point of `B` is already killed by its own default residue. Choose a new ordinary prime `q` with
\[
k\not\equiv v\pmod q\quad(v\in V)
\tag{15}
\]
and assign `r_q=k mod q`. Such a prime exists because all differences in (15) are nonzero and there are only finitely many assigned primes. This kills `k` permanently while preserving `U`, `2`, and all installed forced holes at this new coordinate. It does not enlarge `V`.

Interleave these operations so that infinitely many special coordinates are installed, every prime undergoes residue filling, and every integer other than two is processed. For example, in round `j` install a special coordinate, fill the `j`th prime, and process the `j`th member of a fixed enumeration of `Z\{2}`. A prime frozen earlier as ordinary is never subsequently promoted to special; there are always fresh primes for (11).

Let `U_infinity` be the union of the retained sets and let `r` be the completed default phase. Every installed retained point avoids every eventual `r_q`, and so does `2`. Conversely, if `k!=2` is never installed, the integer-processing operation gives it a permanent default exclusion. Thus
\[
C(r)=U_\infty\sqcup\{2\}.
\tag{16}
\]
The filling operations install infinitely many distinct points. All of `U_infinity` avoids every missing set (6), whereas `2` fails at every special prime. Hence, defining the **actual** support by
\[
S=\{k:k\bmod q\notin M_q\text{ for every prime }q\},
\tag{17}
\]
gives `S=U_infinity`. This equality is justified by the integer-processing step; no unexamined survivors are discarded. Permanent residue witnesses from (14) prove the exact residue profiles in (7). The invariants prove (8), including at all primes introduced after a particular `b_j` was installed.

## 4. Infinite incompatibility without a finite obstruction

Equation (17) and the exact residue profiles imply `cl_pr(S)=S`. Any phase preserving `S` chooses from (6). At every ordinary prime its choice is forced to be `r_q`. To exclude every `b_j`, (8)--(9) force the default residue at every special prime as well. That leaves precisely the default phase `r`, whose support is `T=S union {2}`. Therefore no phase realizes `S`.

For each `p_j in A`, change just that coordinate:
\[
r^{(j)}_q=\begin{cases}2\bmod p_j,&q=p_j,\\r_q,&q\ne p_j,\end{cases}
\qquad C_j=C(r^{(j)}).
\tag{18}
\]
Both available choices at `p_j` preserve `S`, so `S subset C_j`, and the changed choice kills `2`. If `k notin S` and `k!=2`, (16) supplies a default exclusion prime `q_k`. For every `j` with `p_j!=q_k`, that witness still kills `k`. Thus `1_(C_j) -> 1_S` pointwise. Given finite `H subset Z\S`, choose `p_j` outside the finite set of witnesses for `H\{2}`. Equation (18) proves (4).

In the product `R_S`, the constraints excluding `b_j` are the clopen conditions `r'_(p_j)=r_(p_j)`. Their joint solution is the single default phase. The constraint excluding `2` is
\[
E_2=\bigcup_j\{r'\in R_S:r'_{p_j}=2\bmod p_j\},
\tag{19}
\]
the open dense complement of that point. Any finite collection of the forced-coordinate constraints meets (19), but their entire intersection does not. Compactness does not apply to an arbitrary family of open constraints, and Baire's theorem does not turn the non-dense clopen forced-coordinate constraints into dense sets.

There is a useful exact boundary. If **every** hole of a rooted admissible support has finite `W_h(S)`, its exclusion event
\[
E_h=\bigcup_{p\in W_h(S)}\{r'\in R_S:r'_p=h\bmod p\}
\tag{20}
\]
is clopen. Then (4) is the finite-intersection property for closed subsets of the compact space `R_S`, and it **does** imply exact compatibility. No uniform bound on the finite cardinalities is required. The present counterexample instead has the single infinite-witness constraint (19) conflicting with the countable family in (9). This selected family already prevents any solution, irrespective of the other holes.

## 5. What the Cauchy operators retain

For admissible supports the operators (5) are uniformly bounded, by
[[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]], §3. For this fixed kernel, pointwise support convergence in (18) gives strong operator convergence by that finding's column-tail argument. Equivalently, if `D_C` is the diagonal support projection and `H` the bounded discrete Cauchy convolution on `ell^2(Z)`, then `L_C=D_C H D_C`; pointwise masks give `D_(C_j) -> D_S` strongly and hence `L_(C_j) -> L_S` strongly.

Because zero is retained, the nonzero entries of `L_S e_0` identify exactly the nonroot members of `S`. Equality `L_C=L_S` for a rooted compatible support would force `C=S`, which has been disproved. Nevertheless
\[
\inf_{C\in\mathcal C_0,\ S\subset C}
\|(L_C-L_S)e_0\|=0.
\tag{21}
\]
This is a different regime from PC-472, where every compatible completion preserving its particular support retains one of two bounded holes and has a uniform positive column-zero gap. Here the witnesses forced to reappear can escape every fixed window. The exact-image obstruction can therefore be invisible to any finite collection of strong-operator probes, even when every approximant preserves the entire target support.

Neither (21) nor strong convergence implies equality of spectra, preservation of spectral type, or convergence in operator norm. The construction chooses residues and representatives; it does not supply a canonical phase selected by the original circle geometry.

## 6. Prior art, mathematical delta and audit boundary

The group/window coding itself is classical: S. Kasjan, G. Keller and M. Lemańczyk, *Dynamics of B-free sets: a view through the window*, **IMRN 2019**, 2690–2734, DOI [10.1093/imrn/rnx196](https://doi.org/10.1093/imrn/rnx196), [author manuscript](https://arxiv.org/pdf/1702.02375), §1.1. We use its all-primes specialization with retained-root phases and the opposite sign convention for forbidden residues.

G. Keller, *Generalized heredity in B-free systems*, **Stochastics and Dynamics 21** (2021), article 2140008, DOI [10.1142/S0219493721400086](https://doi.org/10.1142/S0219493721400086), [manuscript](https://arxiv.org/pdf/1704.04079), §1.1, Theorem 1 and Corollary 1, separates the exact coding image from its closed hull. Heredity of that hull does not imply heredity of the exact image or finite consistency inside the restricted product (3).

The abstract obstruction in (19) is established infinite-choice geometry. P. J. Cameron, *Hall's marriage theorem*, **Journal of the London Mathematical Society 113** (2026), article e70378, DOI [10.1112/jlms.70378](https://doi.org/10.1112/jlms.70378), §8, recalls the classical family consisting of all positive integers and all its singleton subsets: every finite subfamily has distinct representatives, while the singletons exhaust all choices in the infinite family. The parallel is structural; ordinary residue exclusion is not generally a distinct-representative problem, since one residue can kill multiple holes. The proof here does not invoke a matching theorem.

The additional line-local content is the simultaneous realization of that obstruction by actual integer offsets with the **exact** residue profiles (7), together with `C(r)=S union {2}` and approximation by compatible supersets. An abstract unsatisfiable constraint family or an arbitrarily long finite sieve is insufficient: untested primes could otherwise remove the allegedly forced holes. Sections 3--4 supply the needed all-prime realization and eliminate extra default survivors. PC-472's finite conflict and PC-471's approximation by finite truncations do not establish these conclusions.

Targeted local duplication searches covered finite consistency, finite obstructions, compatible phase selection and infinite exclusion. External checks covered B-free coding images and heredity, infinite representative systems, and the compactness distinction between finite and infinite clauses. The result is classified as a classical-method realization, not a historically new selection theorem. It requires CRT, infinitely many primes avoiding finitely many divisors, and permanent assignments; prime-reciprocal divergence, zeta identities and actual prime-tuple occurrence do not enter.

An exact-integer audit under `/tmp` exercised four special-coordinate stages under each of two deterministic missing-residue policies, interleaving residue filling and integer removal. The runs retained **97** and **147** points, assigned **27** and **37** prime coordinates, and saturated **seven** distinct prime residue profiles each. All **104** invariant checks, **510** completed-profile rechecks, and **eight** finite forced-hole exclusion tests passed; coordinates reached **62** digits. These diagnostics check CRT prescriptions and permanent finite invariants, not the infinite theorem.

The proof is not Lean-verified or independently adversarially approved. Its decisive audit points are the freeze-before-growth cardinality bound, existence of fresh primes satisfying (11) and (15), preservation of both missing residues at every special prime, saturation at all primes, and enumeration of all integers to prove (16). A bounded finite computation cannot establish (9) for every prime. No compute or formalization executor is enrolled: the finite contradiction alone omits the load-bearing infinite realization. This closes the finite-hole-certificate question and leaves the general exact-image characterization open.
