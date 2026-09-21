# MI-055 — Regular Wang multiclusters add Hermite-jet capacities

**Evidence level:** exact synthesis from [VIS-359](../../findings/VIS-359-regular-multicluster-hermite-jet-capacity.md), extending the one-cluster occupancy-width law of VIS-358.

Fix asymptotic depth `q`, distinct positive cluster centers `c_l`, regular equally spaced cluster widths `epsilon_l`, occupancies `N_l`, and the current unweighted Euclidean coefficient norm. If nonnegative Hermite multiplicities `m_l` satisfy `sum_l m_l=q`, then the fixed-depth Wang tail matrix obeys

`s_q(A)^2 >= C min_(l:m_l>0) N_l epsilon_l^(2(m_l-1))`.

Different separated clusters therefore pool local Taylor/Hermite information: cluster `l` can contribute its first `m_l` jets provided its deepest assigned jet mass does not vanish. Conversely, if integers `r_l>=1` have `sum_l r_l<=q-1` and `N_l epsilon_l^(2r_l)->0` for every cluster, the fixed polynomial

`Q(x)=prod_l (x-c_l)^(r_l)`

produces a collapsing direction, so `s_q(A)->0`.

For power-law occupancy `N_l asymp epsilon_l^(-2a_l)`, define the integer jet capacity

`kappa_l=floor(a_l)+1`.

Then the regular separated family has an exact fixed-depth dichotomy: `sum_l kappa_l>=q` gives a uniform positive quotient floor, while `sum_l kappa_l<=q-1` gives collapse. Splitting a dense compact bank among several separated clusters therefore creates no hidden source-free resource; occupancy purchases local derivative jets and those capacities add until the degree-`q-1` polynomial is determined.

The compact frontier is consequently not generic “multicluster interaction.” It is failure of this regular Hermite ledger: irregular rescaled sampling Grams, nonuniform weights or a changed coefficient norm, centers whose separations also collapse, or another resource outside fixed-depth separated Euclidean sampling.

**Boundary.** VIS-359 does not classify arbitrary irregular point clouds, collapsing inter-center separations, nonuniform weights, growing `q`, or infinite-dimensional coefficient topologies. Those remain distinct mechanisms rather than exceptions inferred from the regular theorem.