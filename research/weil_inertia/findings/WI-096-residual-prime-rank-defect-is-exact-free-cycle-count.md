# WI-096 — Residual prime Ramanujan rank defect is exactly the free-cycle count minus one

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes a piece of proof slack left explicitly open in WI-088--WI-095: in the close-prime residual regime, the partial-bijection equations used there are not merely necessary conditions for the true Ramanujan row kernel. Together with the zero-mean condition they are already sufficient. Consequently the residual pairwise rank defect is exactly the number of free directed cycles of the WI-088 partial map, minus the single zero-mean relation.

Let `p<q<2p` be distinct odd primes, put

\[
d=q-p,
\]

and let `delta=delta_N(p,q)` be the nearest-`pq` boundary length. Work in WI-088's genuinely residual exceptional strip

\[
\boxed{
\delta=kq+s,
\qquad
\delta>q-1,
\qquad
d<s<p.
}
\tag{1}
\]

Let

\[
G_{p,q}^{(N)}=(U_p^{(N)})^*U_q^{(N)}
\]

be the primitive-frequency cross Gram and

\[
\tau_{p,q}(\delta)
=(p-1)-\operatorname{rank}G_{p,q}^{(N)}
\tag{2}
\]

its residual row-rank defect. Use the intervals from WI-088

\[
A=\{0,\ldots,s-d-1\},
\qquad
C=\{s-d,\ldots,s-1\},
\qquad
B=\{s,\ldots,p-1\},
\tag{3}
\]

with `D=A union B`, the forced-zero set

\[
Z=kd+\{0,1,\ldots,d-1\}\pmod p,
\tag{4}
\]

and the partial bijection

\[
g(j)=
\begin{cases}
j+(k+1)d,&j\in A,\\
j+kd,&j\in B
\end{cases}
\pmod p.
\tag{5}
\]

WI-088 proves that

\[
g:D\longrightarrow (\mathbf Z/p\mathbf Z)\setminus Z
\tag{6}
\]

is a bijection. Its directed graph is therefore a disjoint union of paths starting in `Z` and ending in `C`, together with directed cycles disjoint from `Z`. Let `c=c(p,q;k,s)` be the number of those free cycles.

Then the exact defect formula is

\[
\boxed{
\tau_{p,q}(\delta)=\max\{0,c-1\}.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
\operatorname{rank}G_{p,q}^{(N)}
=(p-1)-\max\{0,c-1\}.
}
\tag{8}
\]

Thus the inequality `tau <= max(0,c-1)` used in WI-088--WI-095 is always an equality. There are no additional hidden row-kernel constraints left in the omitted equal-residue-sum equations.

## 1. Exact row-kernel model

WI-088 represents a vector in the `p`-frequency row kernel by a `p`-periodic function

\[
f=(f_0,\ldots,f_{p-1}),
\qquad
\sum_{r\bmod p}f_r=0.
\tag{9}
\]

For `0<=j<q`, define the `q` residue-class sums

\[
S_j=
\begin{cases}
\displaystyle\sum_{\ell=0}^{k}f_{j+\ell d},&0\le j<s,\\[3mm]
\displaystyle\sum_{\ell=0}^{k-1}f_{j+\ell d},&s\le j<q,
\end{cases}
\tag{10}
\]

where the indices of `f` are read modulo `p`. Orthogonality to every nontrivial `q`-frequency is exactly

\[
S_0=S_1=\cdots=S_{q-1}.
\tag{11}
\]

From (11), WI-088 selected the following consequences:

\[
\boxed{f_{j+kd}=0\qquad(0\le j<d),}
\tag{12}
\]

\[
\boxed{f_{j+(k+1)d}=f_j\qquad(0\le j<s-d),}
\tag{13}
\]

and

\[
\boxed{f_{j+kd}=f_j\qquad(s\le j<p).}
\tag{14}
\]

Equations (12)--(14) are exactly `f|_Z=0` and `f(g(j))=f(j)` on `D`. WI-088 deliberately used only the forward implication `(11) => (12)--(14)` and therefore treated the graph solution space as a possible strict superset of the true row kernel. The new point is the converse.

## 2. Every sink in `C` is already forced to zero

Because `g:D -> V\Z` is a bijection on `V=Z/pZ`, every vertex has indegree one except the vertices of `Z`, and every vertex has outdegree one except the vertices of `C`. Hence every noncyclic component is a directed path whose source lies in `Z` and whose sink lies in `C`.

Assume (12)--(14). Equation (12) makes the value at every path source zero, and the edge relations (13)--(14) propagate that zero along the entire path. Therefore every path sink is zero as well:

\[
\boxed{f_j=0\qquad(s-d\le j<s).}
\tag{15}
\]

This elementary endpoint observation is the missing converse ingredient. It uses no new Fourier estimate and no generic-position hypothesis.

## 3. The selected equations force all `q` residue sums to be equal

For `0<=j<p`, compare `S_j` with `S_{j+d}`. There are three cases.

If `0<=j<s-d`, both sums are long. Telescoping gives

\[
S_{j+d}-S_j=f_{j+(k+1)d}-f_j=0
\tag{16}
\]

by (13).

If `s-d<=j<s`, the first sum is long and the second is short, so

\[
S_{j+d}-S_j=-f_j=0
\tag{17}
\]

by (15).

If `s<=j<p`, both sums are short and

\[
S_{j+d}-S_j=f_{j+kd}-f_j=0
\tag{18}
\]

by (14). Thus

\[
\boxed{S_{j+d}=S_j\qquad(0\le j<p).}
\tag{19}
\]

It remains only to supply the wraparound steps modulo `q`. For `p<=j<q`, write `j=r+p` with `0<=r<d`. Since `r<d<s<p`, the sum `S_r` is long and `S_{r+p}` is short. By `p`-periodicity of `f`,

\[
S_r-S_{r+p}=f_{r+kd}=0
\tag{20}
\]

using (12). Since `q=p+d`, equation (20) is exactly

\[
S_{j+d-q}=S_j
\qquad(p\le j<q).
\tag{21}
\]

Combining (19) and (21),

\[
\boxed{S_{j+d\bmod q}=S_j\qquad(j\bmod q).}
\tag{22}
\]

Finally,

\[
\gcd(d,q)=\gcd(q-p,q)=\gcd(p,q)=1,
\tag{23}
\]

so addition by `d` is a single cycle on `Z/qZ`. Equation (22) therefore forces

\[
S_0=S_1=\cdots=S_{q-1}.
\tag{24}
\]

This proves the converse `(12)--(14) => (11)`. Hence the WI-088 selected graph equations, together with the already-present zero-mean condition (9), describe the true row kernel exactly.

## 4. Exact dimension is the free-cycle count minus one

The partial-bijection graph consists of zero paths and free cycles. Under (12)--(14), every path is identically zero, while on each free cycle `C_i` the function is an arbitrary constant `a_i`. Before imposing (9), the solution space therefore has exactly one complex degree of freedom per free cycle:

\[
\dim= c.
\tag{25}
\]

If `c=0`, the only solution is zero. If `c>0`, the zero-mean equation becomes

\[
\sum_{i=1}^{c}|C_i|a_i=0.
\tag{26}
\]

This is a nonzero linear functional because every cycle length `|C_i|` is a positive integer. It removes exactly one dimension. Hence

\[
\dim\ker_{\rm row}G
=
\max\{0,c-1\},
\tag{27}
\]

which is (7).

The recently added Lean formalization associated with WI-088 (`WI088PartialBijection`, `WI088PrimePartialMap`, `WI088ResidualPrimeRank`) formalizes the partial-bijection upper-bound route and the residual prime rank floor. It does not currently formalize the converse (22)--(24), so the present theorem is an exact mathematical deduction with a short, isolated future formalization target rather than a claim of kernel-checked completion.

## 5. Consequences for WI-088--WI-095

The first consequence is a decisive closure of one apparent source of slack. WI-088 repeatedly kept the qualification that the full equations (11) "can only shrink the space further." They never do. Therefore a stronger universal prime pairwise rank lower bound cannot be obtained merely by returning to the residue-sum equations discarded in the passage to the partial map. Any improvement must prove that the partial map itself has fewer free cycles.

Second, the resonance mechanism of WI-095 is now an exact description of where true defect dimensions live, rather than a necessary condition extracted from a potentially larger auxiliary space. If `tau>0`, then

\[
\boxed{c=\tau+1.}
\tag{28}
\]

Every one of those `tau+1` free cycles obeys its own closure congruence

\[
p\mid \ell k+a,
\tag{29}
\]

with its length `ell` and number `a` of visits to `A`. The low-denominator hierarchy of WI-095 therefore has no hidden loss at the graph-to-kernel interface. Membership in a resonance layer is still only necessary for a cycle to exist; the new result does **not** make the scalar quotient condition sufficient.

Third, at the canonical opposite-residue one-third boundary, WI-091 explicitly enumerates

\[
r=\frac{2p-q}{3}
\tag{30}
\]

free three-cycles at the center `e=0`. They use all `3r=2p-q` vertices available to free cycles. Thus `c=r`, and (7) gives immediately

\[
\tau=r-1=\frac{2p-q-3}{3}.
\tag{31}
\]

So the **rank statement** of the sharp WI-087/WI-089 center has an alternative purely combinatorial proof once the explicit three-cycle decomposition is known. The Loewner--Bezout representation remains valuable for the rational-interpolation structure and for the shifted exact triangular layer of WI-091; it is simply no longer required to certify the central rank value.

The exact graph also explains non-three-cycle defects. For example, at

\[
(p,q,\delta)=(17,19,65),
\qquad
k=3,
\qquad
s=8,
\tag{32}
\]

the partial map has three free cycles, all of length five, hence (7) gives `tau=2`. This is a concrete denominator-five realization of the higher-resonance sector isolated abstractly by WI-095.

## 6. Falsification and prior-art audit

The load-bearing converse is only (15)--(24). It was stress-tested directly against the exact finite row-kernel system, including the previously recorded examples `(11,13,46)`, `(11,13,47)`, the five-cycle example `(17,19,65)`, the sharp center `(17,19,107)`, and `(19,23,147)`. Exact rational matrix ranks agree with `max(0,c-1)` in each case. A broader finite sweep over close prime pairs and admissible exceptional boundaries found no discrepancy; these computations are falsification only and are not used as proof.

The surrounding literature was re-audited before treating (7) as a new Mathia deduction. Vaidyanathan's 2014 Ramanujan-subspace papers supply the exact-period subspace framework. Tao's prime cyclic uncertainty principle and the Chebotarev Fourier-minor literature control full-spark prime Fourier behavior. Loukaki's 2025 `pq` work and Zhou's 2026 principal-nonsingularity work address composite-order Fourier minors under additional structural hypotheses. These sources are relevant context for rank and finite Fourier geometry, but the located theorem statements concern Fourier-minor nonsingularity/uncertainty rather than the present nearest-`pq` finite-window cross Gram, its residue-sum reduction, or the exact free-cycle dimension formula (7). The targeted search also did not locate this exact equivalence in the Ramanujan-subspace literature. This negative search is **not** used as a claim of priority.

The proof itself depends only on the exact row-kernel model and partial-bijection identities already established in WI-081/WI-088, plus elementary graph structure and `gcd(p,q)=1`. No conjectural prime distribution, random-matrix heuristic, numerical rank tolerance, or unproved Yang input enters (7).

## 7. Program consequence

The residual **prime pairwise rank** problem is now reduced exactly to a finite combinatorial dynamical invariant:

\[
\boxed{
\text{Ramanujan rank defect}
=
\text{number of free cycles of }g
-1
}
\tag{33}
\]

when free cycles exist. This makes a clean stopping rule for the current scalar pairwise route. There is no additional rank gain hidden in the full residue equations beyond the partial-bijection model, while WI-088 shows the cycle count has a sharp one-third ceiling, WI-095 confines extensive cycle counts to low-denominator boundary resonances, and WI-092--WI-094 show extensive-defect edges are metrically weak and have vanishing dyadic cumulative Hilbert--Schmidt coherence.

Accordingly, further work that merely re-solves the same prime pairwise rank equations in Vandermonde, cyclotomic, Loewner, or residue-sum coordinates is unlikely to change the program. A substantive next step must use simultaneous/source-labelled consistency of multiple pair interactions, the low-/zero-defect sector, cross-scale structure, or the full locked four-prime covariance rather than expecting omitted pairwise equations to remove the residual cycles.